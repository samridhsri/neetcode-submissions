
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)

        result = []

        while queue:
            level = []
            
            queueLength = len(queue)

            for i in range(queueLength):
                curr = queue.popleft()

                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if level:
                result.append(level)
        
        return result

        