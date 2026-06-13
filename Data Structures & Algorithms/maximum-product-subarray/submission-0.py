class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Kadane's Algorithm

        max_prod, min_prod = nums[0], nums[0]
        res = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod
            
            min_prod = min(num, min_prod * num)
            max_prod = max(num, max_prod * num)

            res = max(res, max_prod)
        
        return res
