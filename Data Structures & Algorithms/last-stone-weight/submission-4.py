class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Since heapify makes minHeap, we are going to change all the elements to negative to make it work like maxHeap
        for i in range(0, len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:

            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x==y:
                continue
            
            elif x<y:
                y = y - x
                heapq.heappush(stones, -y)
        
        return -stones[0] if stones else 0