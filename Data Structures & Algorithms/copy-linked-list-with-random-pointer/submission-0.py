"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        start = head
        dem_head = Node(start.val)
        dem = dem_head
        dic = {id(start):dem}
        while start.next:
            start = start.next
            de = Node(start.val)
            dic[id(start)] = de
            dem.next = de
            dem = dem.next
        start = head
        while start:
            if not start.random:
                start = start.next
                continue
            temp = dic[id(start)]
            temp2 = dic[id(start.random)]
            temp.random = temp2  
            start = start.next
        return dem_head    