class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for _ in range(len(nums)+1)]

        numToFreq = {}

        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        
        for key, value in numToFreq.items():
            bucket[value].append(key)
        
        result = []

        for i in range(len(bucket)-1, -1, -1):
            for item in bucket[i]:
                result.append(item)
                if len(result) >= k:
                    return result
        
        return result

        