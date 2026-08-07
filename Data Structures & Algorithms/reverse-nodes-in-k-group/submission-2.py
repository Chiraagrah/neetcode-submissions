# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0,head)
        while True:
            tempNode = groupPrev
            for _ in range(k):
                tempNode = tempNode.next
                if not tempNode:
                    return dummy.next
            target = tempNode.next
            prev, curr = groupPrev, groupPrev.next
            
            while curr != target:
                temp = curr.next
                curr.next = prev
                prev,curr = curr, temp
            
            newHead = groupPrev.next
            groupPrev.next = prev
            newHead.next = curr
            groupPrev = newHead