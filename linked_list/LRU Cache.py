class DoubleLinkedList:
    def __init__(self, val, key, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


def remove(node: DoubleLinkedList) -> None:
    prev, _next = node.prev, node.next
    prev.next, _next.prev = _next, prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # create left and right node to keep track of lru and mru
        self.left, self.right = DoubleLinkedList(0, 0), DoubleLinkedList(0, -1)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node: DoubleLinkedList) -> None:
        prev, _next = self.right.prev, self.right
        _next.prev = prev.next = node
        node.next, node.prev = _next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            remove(self.cache[key])
        # re-initialize, if diff val for same key
        self.cache[key] = DoubleLinkedList(val=value, key=key)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            remove(lru)
            del self.cache[lru.key]
        return


if __name__ == '__main__':
    obj = LRUCache(2)
    print(obj.put(2, 1),
          obj.put(2, 2),
          obj.get(2),
          obj.put(1, 1),
          obj.put(4, 1),
          obj.get(2),
          )
