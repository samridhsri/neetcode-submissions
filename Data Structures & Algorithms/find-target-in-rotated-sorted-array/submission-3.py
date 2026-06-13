class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while(l<=h):
            mid = (l+h)//2

            if(nums[mid]==target):
                return mid

            # Check if left part is sorted
            elif (nums[l]<=nums[mid]):

                if(nums[l]<= target and target<nums[mid]):
                    h = mid - 1
                
                else:
                    l = mid + 1
            
            else:
                # Check right part sorted

                if(nums[mid]<target and target<=nums[h]):
                    l = mid + 1
                else:
                    h = mid - 1
        
        return -1


