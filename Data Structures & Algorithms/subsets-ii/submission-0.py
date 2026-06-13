class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # The idea is to include or not include and also sort the whole thing

        result = []
        curSet = []
        nums.sort()

        def helper(i):
            if i >= len(nums):
                result.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(i+1)
            
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i = i + 1
            

            curSet.pop()
            helper(i+1)
        
        helper(0)
        return result