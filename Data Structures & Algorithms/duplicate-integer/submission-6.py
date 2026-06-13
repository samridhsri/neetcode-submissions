class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checkDuplicates = set()

        for num in nums:
            if num in checkDuplicates:
                return True
            checkDuplicates.add(num)
        
        return False