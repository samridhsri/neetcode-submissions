class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result=set()

        for i in range(0, len(nums)-2):

            left = i+1
            right = len(nums)-1

            target = -nums[i]

            while left < right:

                if(nums[left] + nums[right] == target):
                    result.add(tuple(sorted([nums[left],nums[right],nums[i]])))
                    left, right = left+1, right-1
                
                elif(nums[left] + nums[right] < target):
                    left+=1
                
                else:
                    right-=1
        
        return list(result)
