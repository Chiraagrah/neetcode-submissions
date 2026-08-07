# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        que = deque([root])
        while que:
            le = len(que)
            for i in range(le):
                node = que.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
        return result