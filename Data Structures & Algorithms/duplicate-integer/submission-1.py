class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_new = []
        for num in nums:
            if(num in num_new):
                return True
            num_new.append(num)
        return False
         