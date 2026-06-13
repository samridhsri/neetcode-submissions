class Solution:
    def climbStairs(self, n: int) -> int:
        
        # We will start from 0 and choose if take 1 step or 2

        # memoization
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        
        return dfs(0)