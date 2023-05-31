from typing import Optional, Tuple

from linked_list.Reverse_Linked_List import ListNode


def reverse_ll(head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]:
    curr, prev = head, tail.next

    while curr != tail:
        # switch pointers
        next_node = curr.next
        curr.next = prev

        # update prev
        prev = curr

        # increment
        curr = next_node

    curr.next = prev  # for tail

    return curr, head


def k_th_position(k: int, prev: ListNode) -> Tuple[ListNode, int]:
    count, tail = k, prev

    while count and tail.next:
        tail = tail.next
        count -= 1

    return tail, count


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(-1, head)
    curr, group_prev = dummy.next, dummy

    while curr:
        tail, count = k_th_position(k, group_prev)

        if count != 0:
            break

        group_start, group_end = reverse_ll(curr, tail)

        # connect reversed grp
        group_prev.next = group_start

        # increment
        curr = curr.next
        group_prev = group_end

    return dummy.next


def create_linked_list(arr):
    head = ListNode(0, None)
    curr = head
    for i in arr:
        curr.next = ListNode(i, None)
        curr = curr.next
    return head.next


if __name__ == '__main__':
    linked_lists = create_linked_list([1, 2, 3, 4, 5])
    _curr = linked_lists
    while _curr:
        print(_curr.val, end=' -> ')
        _curr = _curr.next
    print("\n------------------")
    reversed_list = reverse_k_group(linked_lists, 2)
    while reversed_list:
        print(reversed_list.val, end=' -> ')
        reversed_list = reversed_list.next
