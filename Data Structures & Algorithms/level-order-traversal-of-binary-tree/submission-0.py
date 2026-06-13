# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = []
        while queue:
            sizeOfQueue = len(queue)

            levels = []

            for i in range(0,sizeOfQueue):

                current = queue.popleft()
                levels.append(current.val)

                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
            if levels:
                result.append(levels)
        
        return result
                

        