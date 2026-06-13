class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique = set()

        for element in nums:
            if element in unique:
                return True
            unique.add(element)
        return False