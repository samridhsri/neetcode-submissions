class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        curSet = []

        def helper(i, curSum):
            if curSum > target:
                return
            
            if curSum == target:
                result.append(curSet.copy())
                return
            
            if i >= len(nums):
                return
            
            # Include till we get target
            curSet.append(nums[i])
            helper(i, curSum+nums[i])

            curSet.pop()
            helper(i+1, curSum)
        
        helper(0,0)
        return result