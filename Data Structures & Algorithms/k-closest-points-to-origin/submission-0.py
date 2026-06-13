class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for point in points:
            x, y = point
            distance = math.sqrt(x*x + y*y)

            heapq.heappush(heap, (distance, point))
        
        result = []

        for j in range(0, k):
            res = heapq.heappop(heap)
            result.append(res[1])
        
        return result