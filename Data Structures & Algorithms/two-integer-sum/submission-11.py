class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numToIndex = {}

        for i in range(len(nums)):
            toFind = target - nums[i]

            if toFind in numToIndex:
                return [numToIndex[toFind], i] if numToIndex[toFind] < i else [i,numToIndex[toFind]]
            
            numToIndex[nums[i]] = i
        
        