class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort() # we need to sort because the output should not contain duplicate result
        for i in range(0, len(nums)):

            for j in range(i+1, len(nums)):

                for k in range(j+1, len(nums)):

                    if(nums[i] + nums[j] + nums[k] == 0):
                        tmp = [nums[i],nums[j],nums[k]]
                        result.add(tuple(tmp))
        
        return [list(i) for i in result]