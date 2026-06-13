# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxOutOfPandQ = max(p.val, q.val)
        minOutOfPandQ = min(p.val, q.val)

        if not root or not p or not q:
            return None
        
        if root.val > maxOutOfPandQ:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif root.val < minOutOfPandQ:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root
        
