class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = [1] * len(nums)

        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [1]
        
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] * nums[i-1]
        
        for j in range(len(post) - 2, -1, -1):
            post[j] = post[j+1] * nums[j+1]
        
        for k in range(0, len(res)):
            res[k] = pre[k] * post[k]
        
        return res