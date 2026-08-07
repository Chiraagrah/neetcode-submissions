# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result=0
    def dfs(self,root,maxval):
        if not root:
            return
        if root.val >= maxval:
            maxval = root.val
            self.result += 1
        self.dfs(root.left,maxval)
        self.dfs(root.right,maxval)
    def goodNodes(self, root: TreeNode) -> int:  
        self.dfs(root,-math.inf)
        return self.result
