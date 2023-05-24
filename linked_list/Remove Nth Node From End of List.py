from typing import Optional

from linked_list.Reverse_Linked_List import ListNode, get_sample_list_node


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """t O(n + n) / S O(1)"""
    if not head and not head.next:
        return
    _current, count = head, 0
    while _current:
        count += 1
        _current = _current.next

    pos, _current = count - n - 1, head
    count = 0
    while _current:
        if count == pos:
            if _current.next:
                _next = _current.next.next if _current.next.next else None
                if _next:
                    _current.next = _next
                else:
                    _current.next = None
            return head
        count += 1
        _current = _current.next
    return head


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """t O(n) / s O(1)"""
    if not head and not head.next:
        return
    # create dummy node before head if in case have to remove head
    dummy = ListNode(0)
    dummy.next = head

    # move fast until, to find appropriate position to remove nth node
    fast = dummy
    for _ in range(n):
        fast = fast.next

    slow = dummy
    while fast.next:
        slow = slow.next
        fast = fast.next

    if slow.next:
        slow.next = slow.next.next if slow.next.next else None
    return dummy.next


if __name__ == '__main__':
    head = get_sample_list_node()
    current = head
    while current is not None:
        print(current.val, end=' -> ')
        current = current.next

    # Reverse the linked list
    new_head = remove_nth_from_end(head, 6)

    # Print the reversed linked list
    current = new_head
    print()
    while current is not None:
        print(current.val, end=' -> ')
        current = current.next
