class Solution:
    def checkRange(self, arr: list[int], num):
        if num < arr[0]:
            return -1
        
        elif num > arr[-1]:
            return 1
        
        else:
            return 0
    
    def binarySearch(self, arr: list[int], target):
        left = 0
        right = len(arr) - 1

        while (left <= right):
            mid = (left + right) // 2

            if(arr[mid] == target):
                return True
            
            elif(arr[mid] < target):
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1

        while (left <= right):
            mid = (left + right) // 2

            if(self.checkRange(matrix[mid], target) == 0):
                res = self.binarySearch(matrix[mid], target)
                return res
            
            elif(self.checkRange(matrix[mid], target) == -1):
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False