class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        dic = {None: None}
        
        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = dic[curr]
            copy.next = dic[curr.next]
            copy.random = dic[curr.random]
            curr = curr.next
            
        return dic[head]