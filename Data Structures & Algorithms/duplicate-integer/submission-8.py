class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set()

        for num in nums:
            if num in isDuplicate:
                return True
            
            isDuplicate.add(num)
        
        return False