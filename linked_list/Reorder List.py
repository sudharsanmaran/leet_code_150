from typing import Optional

from linked_list.Reverse_Linked_List import ListNode, get_sample_list_node


def reorderList(head: Optional[ListNode]) -> None:
    """t O(n + n) / s O(1)"""
    if not head and not head.next:
        return

    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse from middle
    _current, prev = slow.next, None
    while _current:
        _next = _current.next
        _current.next = prev
        prev = _current
        _current = _next

    # remove next element after middle
    slow.next = None

    # merge
    p1, p2 = head, prev
    while p2:
        # copy
        _next_p1, _next_p2 = p1.next, p2.next

        # interchange
        p1.next, p2.next = p2, _next_p1

        # increment
        p2, p1 = _next_p2, _next_p1

    return


if __name__ == '__main__':
    head = get_sample_list_node()
    reorderList(head)
    current = head
    while current is not None:
        print(current.val, end=' -> ')
        current = current.next
