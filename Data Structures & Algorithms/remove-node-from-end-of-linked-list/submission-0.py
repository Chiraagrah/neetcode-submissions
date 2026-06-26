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
        strt = head
        prev = None
        while num:
            tem = strt.next
            prev = strt
            strt = tem
            num-=1
        if prev:
            prev.next = strt.next
            return head
        else:
            return head.next
