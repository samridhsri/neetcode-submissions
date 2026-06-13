class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # The idea is to include an element or exclude it

        result = []
        subset = []

        def helper(i):

            # Base case
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Include the element
            subset.append(nums[i])
            helper(i+1) #continue the path

            # Exclude the element
            subset.pop()
            helper(i+1) # continue the path
        
        helper(0)
        return result
