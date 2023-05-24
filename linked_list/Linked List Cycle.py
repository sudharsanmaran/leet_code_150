from typing import Optional

from linked_list.Reverse_Linked_List import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    """t O(n) / s O(1)"""
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow, fast = slow.next, fast.next.next
    return False


if __name__ == '__main__':
    # Create the linked list with a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2  # Create a cycle

    # Test the function
    has_cycle = hasCycle(node1)
    print(has_cycle)  # Output: True

    # Create the linked list without a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Test the function
    has_cycle = hasCycle(node1)
    print(has_cycle)  # Output: False
