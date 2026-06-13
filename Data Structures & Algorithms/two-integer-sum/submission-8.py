class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numToIndex = {}

        for i in range(0, len(nums)):
            toFind = target - nums[i]

            if toFind in numToIndex:
                if i < numToIndex[toFind]:
                    return [i, numToIndex[toFind]]
                else:
                    return [numToIndex[toFind], i]
            numToIndex[nums[i]] = i
        
        