class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Idea is that best rate of k can be the max number of Bananas
        # Therefore, optimize between 1 and maxBananas

        maxBananas = piles[0]
        for p in piles:
            if p > maxBananas:
                maxBananas = p
            
        
        left, right = 1, maxBananas
        res = maxBananas

        while(left <= right):

            k = (left + right) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(int(p) / int(k))
            
            if totalTime <= h:
                res = min(res, k)
                right = k - 1
            
            else:
                left = k + 1
        
        return res