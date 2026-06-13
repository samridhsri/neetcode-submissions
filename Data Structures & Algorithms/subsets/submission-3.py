class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # The idea is to include or not include each element

        result = []
        curSet = []

        def helper(i):
            if i == len(nums):
                result.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(i+1)

            curSet.pop()
            helper(i+1)
        
        helper(0)
        return result
            

