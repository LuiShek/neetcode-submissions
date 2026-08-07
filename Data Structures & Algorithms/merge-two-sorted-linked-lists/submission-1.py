# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = list1
        while curr:
            arr.append(curr.val)
            curr = curr.next
        curr = list2
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr = sorted(arr)

        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        head = dummy.next
        return head


        



        