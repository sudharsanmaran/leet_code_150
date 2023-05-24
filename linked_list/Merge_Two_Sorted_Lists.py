from typing import Optional

from Reverse_Linked_List import ListNode


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    _head = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            _head.next = list1
            list1 = list1.next
        else:
            _head.next = list2
            list2 = list2.next
        _head = _head.next

    # extras
    if list1:
        _head.next = list1
    if list2:
        _head.next = list2

    return dummy.next


def get_sample_list_node_1():
    _head = ListNode(5)
    _head.next = ListNode(8)
    _head.next.next = ListNode(9)
    _head.next.next.next = ListNode(11)
    _head.next.next.next.next = ListNode(13)
    return _head


def get_sample_list_node_2():
    _head = ListNode(2)
    _head.next = ListNode(6)
    _head.next.next = ListNode(7)
    _head.next.next.next = ListNode(9)
    return _head


if __name__ == '__main__':
    head = mergeTwoLists(get_sample_list_node_1(), get_sample_list_node_2())
    current = head
    while current is not None:
        print(current.val)
        current = current.next
