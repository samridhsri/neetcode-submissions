class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        # Convert the numbers array into a set

        numSet = set(nums)
        maxLength = 1
        # Iterate through the array
        
        for num in nums:
            # Check if this number has a left neighbour i.e it is starting of the range or not
            length = 1
            if (num + 1 in numSet):
                length+=1
                num = num + 1
                while num + 1 in numSet:
                    length+=1
                    num = num + 1
                
                maxLength = max(maxLength, length)
        
        return maxLength
                