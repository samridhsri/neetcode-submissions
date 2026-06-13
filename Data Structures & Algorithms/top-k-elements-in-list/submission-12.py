class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # len(nums) + 1 array to get k element
        # For frequency make hashmap

        freqMap = {} # num -> freq
        maxFreq = 0

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
            if freqMap[num] > maxFreq:
                maxFreq = freqMap[num]
        
        arrToGetK = [[] for _ in range(maxFreq+1)]

        for key, value in freqMap.items():
            arrToGetK[value].append(key)
        
        result = []
        
        for i in range(len(arrToGetK)-1, -1, -1):
            for element in arrToGetK[i]:
                if len(result) == k:
                    break
        
                result.append(element)
                
        return result
