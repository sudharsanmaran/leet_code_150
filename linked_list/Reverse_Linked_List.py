from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr is not None:
        # store next
        _next = curr.next
        # change next and prev
        curr.next = prev
        prev = curr
        # increment curr
        curr = _next
    return prev


def get_sample_list_node():
    _head = ListNode(1)
    _head.next = ListNode(2)
    _head.next.next = ListNode(3)
    _head.next.next.next = ListNode(4)
    _head.next.next.next.next = ListNode(5)
    return _head


if __name__ == '__main__':
    head = get_sample_list_node()
    # Print the original linked list
    print("Original linked list:")
    current = head
    while current is not None:
        print(current.val)
        current = current.next

    # Reverse the linked list
    new_head = reverse_list(head)

    # Print the reversed linked list
    print("Reversed linked list:")
    current = new_head
    while current is not None:
        print(current.val)
        current = current.next
