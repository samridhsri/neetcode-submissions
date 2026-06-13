class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # The whole idea is to include or not include

        result = []
        curset = []

        def helper(i):
            if i >= len(nums):
                result.append(curset.copy())
                return
            
            # Include the element
            curset.append(nums[i])
            helper(i+1)

            # Exclude the element
            curset.pop()
            helper(i+1)
        
        helper(0)
        return result