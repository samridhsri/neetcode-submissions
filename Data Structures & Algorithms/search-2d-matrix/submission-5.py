class Solution:

    def checkRange(self, arr: List[int], target):

        if target >=arr[0] and target <= arr[-1]:
            return 0

        elif target > arr[-1]:
            return 1

        else:
            return -1
    
    def binarySearch(self, arr: List[int], target):
        left, right = 0, len(arr) - 1

        while(left <= right):
            mid = (left + right) // 2

            if(arr[mid] == target):
                return True
            
            elif(arr[mid] < target):
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # The idea is to implement binary search for the range then for the element

        left = 0
        right = len(matrix) - 1

        while(left <= right):

            mid = (left + right) // 2

            if(self.checkRange(matrix[mid], target) == 0):
                return self.binarySearch(matrix[mid], target)
            
            elif(self.checkRange(matrix[mid], target) == -1):
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False