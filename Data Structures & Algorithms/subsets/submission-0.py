class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Think of adding or not

        result = []

        curSet = []

        # Helper is going to help us to decide to add the number into subset or not
        def helper(i):
            if i >= len(nums):
                result.append(curSet.copy())
                return
            
            # Add the new number
            curSet.append(nums[i])
            helper(i + 1) # Take that decision to the end

            curSet.pop() # Undo the addition of new number to the set
            helper(i + 1)
        
        helper(0)
        
        return result