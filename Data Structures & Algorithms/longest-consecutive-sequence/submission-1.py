class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        numSet = set(nums)
        maxLength = 1

        for num in nums:
            length = 1
            while (num + 1 in numSet):
                num+=1
                length+=1
            
            maxLength = max(maxLength, length)
        
        return maxLength