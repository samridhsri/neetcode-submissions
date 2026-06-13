class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(arr, target):
            l, r = 0, len(arr) - 1

            while (l <= r):
                mid = (l+r)//2

                if target == arr[mid]:
                    return True
                
                elif target < arr[mid]:
                    r = mid - 1
                
                else:
                    l = mid + 1
            return False

        l, r = 0, len(matrix)-1

        while (l <= r):
            mid = (l+r)//2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return binarySearch(matrix[mid], target)
            
            elif target < matrix[mid][0]:
                r = mid - 1
            
            elif target > matrix[mid][-1]:
                l = mid + 1
        
        return False