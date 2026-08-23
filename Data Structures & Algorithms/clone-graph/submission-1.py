"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        nodedict = {node.val:Node(node.val)}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            copyHead  = nodedict[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in nodedict:
                    nodedict[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                copyneighbor = nodedict[neighbor.val]
                copyHead.neighbors.append(copyneighbor)
                
        return nodedict[node.val]
        