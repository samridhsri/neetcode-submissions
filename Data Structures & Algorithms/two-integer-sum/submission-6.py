class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numberToIndex = {}

        for i in range(len(nums)):
            
            toFind = target - nums[i]

            if toFind in numberToIndex:
                if i < numberToIndex[toFind]:
                    return [i, numberToIndex[toFind]]
                
                else:
                    return [numberToIndex[toFind], i]
            
            numberToIndex[nums[i]] = i 