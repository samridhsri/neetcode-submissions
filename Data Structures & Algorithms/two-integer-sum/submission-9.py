class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        findNum = {}
        for i in range(0, len(nums)):
            curr = target - nums[i]

            if curr in findNum:
                return [i, findNum[curr]] if i<findNum[curr] else [findNum[curr], i]

            findNum[nums[i]] = i

        return [] 