class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)

        res = [0] * size
        pref = [0] * size
        suff = [0] * size

        pref[0] = suff[size-1] = 1

        for i in range(1, size):
            pref[i] = nums[i-1] * pref[i-1]
        
        for i in range(size-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        
        for i in range(size):
            res[i] = pref[i] * suff[i]
        
        return res

        