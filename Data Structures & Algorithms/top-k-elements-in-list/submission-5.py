class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = [[] for _ in range(len(nums)+1)]
        hashMap = {}

        for n in nums:
            freq = hashMap.get(n, 0)
            hashMap[n] = freq + 1
        
        for key, value in hashMap.items():
            count[value].append(key)
        
        result = []

        for i in range(len(count)-1, 0, -1):
            for m in count[i]:
                result.append(m)
                if(len(result)==k):
                    return result
        