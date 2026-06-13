class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = float('-inf')
        for bananas in piles:
            if bananas>maxBananas:
                maxBananas = bananas
        
        l,r = 1, maxBananas
        res = r
        
        while(l<=r):
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