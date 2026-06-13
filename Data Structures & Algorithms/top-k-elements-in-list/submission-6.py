class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range (len(nums)+1)]

        for num in nums:
            # fill out hashMap for frequency
            count[num] = count.get(num,0) + 1 # Key = Number, Value = Frequency
        
        for n,f in count.items():
            buckets[f].append(n)
        
        result = []

        for i in range(len(buckets)-1,0,-1):
            for element in buckets[i]:
                result.append(element)
                if(len(result)==k):
                    return result
