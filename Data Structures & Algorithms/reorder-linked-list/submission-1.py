# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return 

        slow , fast = head , head.next
        while fast and fast.next:
            fast = fast.next.next
            slow  = slow.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp  = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        fin = head
        start = prev

        while start:
            tem = fin.next
            tem2 = start.next

            fin.next = start
            start.next = tem

            start = tem2
            fin = tem
        