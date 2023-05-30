import heapq
from typing import List, Optional

from linked_list.Reverse_Linked_List import ListNode


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """t O(n log n) / s O(n)"""
    heap, res = [], ListNode(0, None)

    for ll in lists:
        curr = ll
        while curr:
            heapq.heappush(heap, curr.val)
            curr = curr.next

    curr = res
    while heap:
        curr.next = ListNode(heapq.heappop(heap), None)
        curr = curr.next

    return res.next if res.next else None


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """t O(n log n) / t O(1)"""
    def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0, None)
        curr = res
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return res.next

    while len(lists) > 1:
        _merged_list = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            _merged_list.append(merge_list(l1, l2))
        lists = _merged_list
    return lists[0] if lists else None


if __name__ == '__main__':
    def create_linked_list(arr):
        # Create a dummy node to serve as the head of the linked list
        dummy = ListNode(0)
        res = []

        # Iterate over the input list and create a linked list
        for sublist in arr:
            curr = dummy
            for val in sublist:
                curr.next = ListNode(val)
                curr = curr.next
            res.append(dummy.next)

        # Return the head of the linked list
        return res


    arr = [[1, 4, 5], [1, 3, 4], [2, 6], [7, 9], [5, 6]]
    linked_lists = create_linked_list(arr)
    merged_list = merge_k_lists(linked_lists)
    while merged_list:
        print(merged_list.val, end=' -> ')
        merged_list = merged_list.next
