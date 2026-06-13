class Solution:
    def checkRange(self, nums: List[int], target: int):
            if nums[0] <= target and nums[-1] >= target:
                return 0
            
            elif target < nums[0]:
                return -1
            
            else:
                return 1
        
    def binarySearch(self, nums: List[int], target: int):

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            
            elif nums[mid] < target:
                start = mid + 1
            
            else:
                end = mid - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            
            if self.checkRange(matrix[mid], target) == 0:
                return self.binarySearch(matrix[mid], target)
            
            elif self.checkRange(matrix[mid], target) == -1:
                end = mid - 1
            
            else:
                start = mid + 1
        return False