class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        dic = {None: None}
        
        # Pass 1: Just create the copies. 
        # No 'if' checks needed inside the loop.
        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
            
        # Pass 2: Just link the pointers.
        curr = head
        while curr:
            copy = dic[curr]
            copy.next = dic[curr.next]
            copy.random = dic[curr.random]
            curr = curr.next
            
        return dic[head]