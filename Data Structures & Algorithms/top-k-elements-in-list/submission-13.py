class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums)+1)]

        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets)-1, -1, -1):

            if len(buckets[i]) == 0:
                continue
            
            
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result