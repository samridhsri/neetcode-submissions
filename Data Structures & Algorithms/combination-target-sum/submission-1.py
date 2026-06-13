class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # I can use each number any number of times

        result = []
        curSet = []

        def helper(i, curSum):
            if curSum == target:
                result.append(curSet.copy())
                return
            
            if i >= len(nums):
                return
            
            if curSum > target:
                return
            
            # Add the current number
            curSet.append(nums[i])
            helper(i, curSum+nums[i])

            # Remove the number
            curSet.pop()
            helper(i+1, curSum)
        
        helper(0,0)
        return result