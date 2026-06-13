class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        nums.sort()

        for i in range(0, len(nums)-2):

            left = i + 1
            right = len(nums)-1
            target = -nums[i]

            while left < right:
                if(nums[left] + nums[right] == target):
                    tmp = tuple(sorted([nums[left], nums[right], nums[i]]))
                    result.add(tmp)
                    left, right = left+1, right - 1
                
                elif(nums[left] + nums[right] < target):
                    left+=1
                
                else:
                    right-=1
            
        return [list(i) for i in result]