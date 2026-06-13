class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        res = nums[0]

        if nums[l] < nums[h]:
            return res

        while(l<=h):
            mid = (l+h)//2
            res = min(nums[mid], res)

            if nums[mid] > nums[l]:
                # Search on right
                res = min(nums[l], res)
                l = mid + 1
            
            else:
                # Search left
                res = min(nums[h], res)
                h = mid - 1
        
        return res
