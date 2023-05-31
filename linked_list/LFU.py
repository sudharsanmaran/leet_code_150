"""https://leetcode.com/problems/lfu-cache/

approach
1. use hashmap to store key and val for constant time lookup
2. also use hash map to store frequency(counter) for that key
2.1 here if multiple node/keys is in low frequencies' quota, need to remove least recently used(LRU), so have to maintain
    doubly linked list to efficiently reorder
3. if new val is added or key is being looked up need to update frequency
4. if capacity of LFU exceeds need to evict lru of min frequency linked list
"""


class Node:
    def __init__(self, key, val, count=1, prev=None, next=None):
        self.key = key
        self.val = val
        self.count = count
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        # auxiliary variable length to store len of ll for constant lookup
        self.length = 0

        # create dummy nodes to avoid edge cases
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)

        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node: Node) -> None:
        self.length += 1

        prev, next = self.tail.prev, self.tail

        #  update pointers
        prev.next, node.next = node, next
        node.prev, next.prev = prev, node

        return

    def remove(self, node: Node) -> None:
        self.length -= 1

        prev, next = node.prev, node.next

        #  update pointers
        prev.next, next.prev = next, prev

        return


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lowest_freq = 1  # auxiliary variable to find apt ll to evict in constant time
        self.key_val = dict()  # key: Node
        self.count_node = dict()  # key: LinkedList

    def update_lowest_freq(self, count):
        self.lowest_freq = count + 1

    def append_node(self, node):
        if node.count in self.count_node:
            next_ll = self.count_node[node.count]
            next_ll.append(node)
        else:
            new_ll = LinkedList()
            self.count_node[node.count] = new_ll
            new_ll.append(node)

    def update_linked_list(self, node):

        curr_count = node.count

        curr_ll = self.count_node[curr_count]

        # remove node from curr_count curr_ll
        curr_ll.remove(node)

        # update node count
        node.count += 1

        if not curr_ll.length:  # update lowest_freq
            self.update_lowest_freq(curr_count)

        self.append_node(node)

    def evict(self):
        low_freq_ll = self.count_node[self.lowest_freq]
        lru = low_freq_ll.head.next
        low_freq_ll.remove(lru)
        del self.key_val[lru.key]
        return

    def get(self, key: int) -> int:
        if key in self.key_val:
            node = self.key_val[key]
            self.update_linked_list(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)  # in case of new value for same key
        if key in self.key_val:
            old_node = self.key_val[key]

            #  update pointers
            new_node.next, new_node.prev = old_node.next, old_node.prev

            # update new val in cache
            self.key_val[key] = new_node

            self.update_linked_list(new_node)
        else:
            self.key_val[key] = new_node
            if len(self.key_val) > self.capacity:
                self.evict()
            self.append_node(new_node)


if __name__ == '__main__':
    obj = LFUCache(3)
    obj.put(2, 2)
    obj.put(1, 1)
    obj.get(2)
    obj.get(1)
    obj.get(2)
    obj.put(3, 3)
    obj.put(4, 4)
    obj.get(3)
    print(obj.get(1), obj.get(3), obj.put(4, 4), obj.get(2), obj.get(4))
