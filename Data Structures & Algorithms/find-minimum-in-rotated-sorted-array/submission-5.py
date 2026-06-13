class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # [4,5,6,1,2,3]
        # [1,2,3,4,5,6]
        # [6,1,2,3,4,5]

        l, r = 0, len(nums)-1
        bestAnswer = nums[l] #6
        
        while(l <= r):
            mid = (l+r) // 2
            if bestAnswer > nums[mid]:
                bestAnswer = nums[mid] #  2
            
            elif nums[mid] < nums[r]:
                r = mid - 1
            
            else:
                l = mid + 1
        if bestAnswer > nums[mid]: bestAnswer = nums[mid]
        
        return bestAnswer
