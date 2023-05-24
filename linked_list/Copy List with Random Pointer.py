from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    """t O(n + n) / s O(n + n)"""

    curr, hash_map = head, dict()
    while curr:
        hash_map[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        cur_new = hash_map[curr]
        cur_new.next, cur_new.random = hash_map.get(curr.next), hash_map.get(curr.random)
        curr = curr.next
    return hash_map.get(head)


if __name__ == '__main__':
    # Create the sample Node objects
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Set the next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Set the random pointers
    node1.random = node3  # node1's random pointer points to node3
    node2.random = node5  # node2's random pointer points to node5
    node4.random = node2  # node4's random pointer points to node2

    # Printing the values and random pointers of the sample Node objects
    current = node1
    while current:
        random_val = current.random.val if current.random else None
        print(f"Value: {current.val}, Random: {random_val}")
        current = current.next
    print('--------------------------')

    head = copyRandomList(node1)

    # Printing the values and random pointers of the sample Node objects
    current = head
    while current:
        random_val = current.random.val if current.random else None
        print(f"Value: {current.val}, Random: {random_val}")
        current = current.next
