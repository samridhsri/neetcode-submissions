class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # optimise
        def tryCurrentSpeed(k):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/k)
            
            if totalTime <= h:
                return True
            return False

        k = piles[0]

        for pile in piles:
            if pile > k:
                k = pile
        
        left, right = 1, k

        while (left <= right):
            k = (left + right) // 2

            if tryCurrentSpeed(k):
                bestAnswer = k
                right = k - 1
            else:
                left = k + 1
        
        return bestAnswer