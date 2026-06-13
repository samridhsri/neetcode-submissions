class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Search for maximum bananas
        maxBananas = float('-inf')
        for p in piles:
            if p > maxBananas:
                maxBananas = p
        
        # We will search for banana eating rate between 1 and maxBananas
        l, r = 1, maxBananas

        res = r

        while l <= r:

            k = (l+r)//2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p)/k)
            
            if totalTime <= h:
                res = k
                r = k - 1
            
            else:
                l = k + 1
        
        return res