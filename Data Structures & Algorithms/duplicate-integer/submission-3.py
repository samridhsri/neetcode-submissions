class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        uniqueNums = set()

        for element in nums:
            if element in uniqueNums:
                return True
            uniqueNums.add(element)
        
        return False