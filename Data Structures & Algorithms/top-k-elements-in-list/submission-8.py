class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # I need to find the K most frequent elements
        # Two ways that I recall of - Heap and Bucket method

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []

        for i in range(len(bucket)-1, -1, -1):
            for element in bucket[i]:
                result.append(element)
            
            if len(result) == k:
                return result