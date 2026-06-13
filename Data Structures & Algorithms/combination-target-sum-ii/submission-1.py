class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # I can use each number at most once

        result = []
        curSet = []
        nums.sort()

        def helper(i, curSum):
            if curSum == target:
                result.append(curSet.copy())
                return
            
            if curSum > target or i >= len(nums):
                return
            
            # Include the current number
            curSet.append(nums[i])
            helper(i+1, curSum + nums[i])
            # Exclude the current number
            curSet.pop()
            
            while (i+1 < len(nums) and nums[i] == nums[i+1]):
                i=i+1
            

            helper(i+1, curSum)
        
        helper(0,0)
        return result