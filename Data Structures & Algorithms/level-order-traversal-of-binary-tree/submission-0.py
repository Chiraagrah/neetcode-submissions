# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        result = []
        temp = deque([root])
        if not root:
            return []
        while temp:
            le  = len(temp)
            level = []
            for _ in range(le):
                node = temp.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                level.append(node.val)
            result.append(level)
        return result