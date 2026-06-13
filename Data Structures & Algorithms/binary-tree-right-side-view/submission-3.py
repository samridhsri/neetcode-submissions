# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # For each level we need the right most

        queue = collections.deque()
        queue.append(root)

        result = []

        while queue:
            queueLength = len(queue)
            level = []
            
            for i in range(queueLength):
                curr = queue.popleft()
                
                if curr:
                    level.append(curr)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if level:
                result.append(level[-1].val)
        
        return result