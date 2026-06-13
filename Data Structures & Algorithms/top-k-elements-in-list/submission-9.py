class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # I need to get the top k elements from the array

        # Lets make an array with freq
        bucket = [[] for _ in range(len(nums)+1)]

        numToFreq = {}

        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        
        for elem, freq in numToFreq.items():
            bucket[freq].append(elem)

        result = []

        for i in range(len(bucket)-1, -1, -1):
            for item in bucket[i]:
                result.append(item)
                if len(result) >= k:
                    return result
        
        return result
