class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for left in range(len(nums) - k + 1):
            maxElement = nums[left]

            for right in range(left, left + k):
                if nums[right] > maxElement:
                    maxElement = nums[right]
            
            res.append(maxElement)
        
        return res