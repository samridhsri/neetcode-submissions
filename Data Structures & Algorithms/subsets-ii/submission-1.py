class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        curSet = []

        def helper(i):
            if i>=len(nums):
                result.append(curSet.copy())
                return
            
            # Idea is to include or not include

            curSet.append(nums[i])
            helper(i+1)

            curSet.pop()

            while(i+1 < len(nums) and nums[i]==nums[i+1]):
                i+=1
            
            helper(i+1)
        
        helper(0)
        return result