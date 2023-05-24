from typing import Optional

from linked_list.Merge_Two_Sorted_Lists import get_sample_list_node_1, get_sample_list_node_2
from linked_list.Reverse_Linked_List import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """t O(max(l1, l2)) / s O(1)"""
    dummy = ListNode(0)
    curr, carry = dummy, 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)

        # increment
        curr, l1, l2 = curr.next, l1.next if l1 else None, l2.next if l2 else None
    return dummy.next


if __name__ == '__main__':
    head = addTwoNumbers(get_sample_list_node_1(), get_sample_list_node_2())
    for current in (get_sample_list_node_1(), get_sample_list_node_2(), head):
        if current == head:
            print('--------------------------------')
        while current is not None:
            print(current.val, end=' -> ')
            current = current.next
        print()

