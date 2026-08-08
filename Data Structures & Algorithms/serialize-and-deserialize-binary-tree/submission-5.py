# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        st = ""
        while queue:
            node = queue.popleft()
            if not node:
                st+="#,"
            else:
                st+=f"{node.val},"
                queue.append(node.left)
                queue.append(node.right)
        return st
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data=='#,':
            return None
        vals = data.split(',')
        print(vals)
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i=1
        while i<len(vals) and queue:
            Node = queue.popleft()
            if vals[i]!='#':
                left = TreeNode(int(vals[i]))
                Node.left = left
                queue.append(left)
            i+=1
            if i<len(vals) and vals[i]!='#':
                right = TreeNode(int(vals[i]))
                Node.right = right
                queue.append(right)
            i+=1
        return root
        

