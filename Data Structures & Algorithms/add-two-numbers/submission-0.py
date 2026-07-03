# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        temp = 1
        while l1:
            num1+= l1.val*temp
            temp*=10
            l1 = l1.next
        temp = 1
        while l2:
            num2 += l2.val*temp
            temp*=10
            l2 = l2.next
        Nod = None
        su = num1+num2
        for x in str(su):
            temp = ListNode(int(x))
            temp.next = Nod
            Nod = temp
        return Nod
        
        
            