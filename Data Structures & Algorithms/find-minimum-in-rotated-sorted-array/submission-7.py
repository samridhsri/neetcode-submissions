class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # [4,5,6,1,2,3]
        # [1,2,3,4,5,6]
        # [6,1,2,3,4,5]

        l, r = 0, len(nums)-1
        
        res = nums[l]
        while(l<=r):
            mid = (l+r)//2

            res = min(nums[mid], res)

            if nums[mid] > nums[r]:
                l = mid+1
            
            else:
                r = mid - 1
        
        return res
