class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Idea is to search the rate k between 1 and maximum number of Bananas

        maxBananas = float('-inf')

        for p in piles:
            if maxBananas < p:
                maxBananas = p
        
        # Apply binary search

        left, right = 1, maxBananas
        res = 1

        while(left <= right):

            k = (left+right) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p)/k)
            
            if(totalTime<=h):
                res = k
                right = k - 1
            
            else:
                left = k + 1
        
        return res