# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, p, q):
        if not p and not q:
            return True
        if ((not p) and q) or ((not q) and p) or p.val != q.val :
            self.result = False
            return False
        left = self.dfs(p.left,q.left)
        right = self.dfs(p.right,q.right)
        return left and right
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        self.dfs(p,q)
        return self.result
        