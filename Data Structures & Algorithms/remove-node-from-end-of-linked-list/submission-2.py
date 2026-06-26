# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        tem = head
        while tem:
            tem = tem.next
            count+=1
        num = count - n
        curr = head
        prev = None
        if num == 0 :
            return head.next
        for _ in range(num):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head
