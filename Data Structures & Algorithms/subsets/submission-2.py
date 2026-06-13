class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # The whole idea is to include or not include each number

        result = []
        curSet = []

        def helper(i):
            if i>=len(nums):
                result.append(curSet.copy())
                return
            
            # Include the number
            curSet.append(nums[i])
            helper(i+1) # complete the path

            # Exclude the number
            curSet.pop()
            helper(i+1) # complete the path
        
        helper(0)
        return result