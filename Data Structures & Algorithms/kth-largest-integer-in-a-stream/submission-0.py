class KthLargest:
    # when we talk about Kth largest then we are talking about Heap
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        # Make the array a heap

        heapq.heapify(self.minHeap)
        
        # Make the mminHeap size k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
