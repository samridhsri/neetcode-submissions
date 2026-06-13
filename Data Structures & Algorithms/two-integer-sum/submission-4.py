class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numberToIndex = {}

        for i in range(0, len(nums)):
            toFind = target - nums[i]
            if toFind in numberToIndex:
                if numberToIndex[toFind] < i:
                    return [numberToIndex[toFind], i]
                return [i, numberToIndex[toFind]]
            
            numberToIndex[nums[i]] = i