class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        bestAnswer = nums[l]

        while(l <= r):

            mid = (l + r) // 2

            bestAnswer = min(nums[mid], bestAnswer)

            if(nums[mid]>nums[r]):
                l = mid + 1
            
            else:
                r = mid - 1
        
        return bestAnswer