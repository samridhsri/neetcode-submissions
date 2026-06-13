"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # We have to create an actual clone of this thing

        # Lets create a hashmap first
        originalToNew = {}

        def dfs(node):

            # Base case
            if node in originalToNew:
                return originalToNew[node]
            
            # Recursive case

            # make a copy
            copy = Node(node.val)
            # Add copy to hashmap
            originalToNew[node] = copy

            # Iterate through all the neighbors of the node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None