# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {v:i for i, v in enumerate(inorder)}
        def build(preorder,inorder,lp,rp,li,ri):
            if lp > rp:
                return None
            node_val = preorder[lp]
            index = hashmap[node_val]
            root = TreeNode(node_val,build(preorder,inorder,lp+1,lp+index-li,li,index-1),build(preorder,inorder,lp+index-li+1,rp,index+1,ri))
            return root
        n = len(preorder)
        root = build(preorder,inorder,0,n-1,0,n-1)
        return root
