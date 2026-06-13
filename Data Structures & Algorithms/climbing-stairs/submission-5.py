class Solution:
    def climbStairs(self, n: int) -> int:
        
        # lets try bottom up approach

        first, second = 1, 2
        
        if n <= 2:
            return n

        for i in range(3, n+1):
            temp = first + second
            first, second = second, temp
        
        return temp