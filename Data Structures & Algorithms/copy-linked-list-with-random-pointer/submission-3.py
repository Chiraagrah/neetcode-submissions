class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        dic = {None:None}
        start = head
        while start:
            if start not in dic:
                dic[start] = Node(start.val)
            temp = dic[start]

            if start.next not in dic:
                dic[start.next] = Node(start.next.val)
            
            if start.random not in dic:
                dic[start.random] = Node(start.random.val)
            
            temp.next = dic[start.next]
            temp.random = dic[start.random]

            start = start.next
        return dic[head]