class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def isCorrect(mid): #check the range of Number
            if(target>matrix[mid][-1]): # if above the range
                return 1
            elif(target<matrix[mid][0]): # below the range
                return -1
            else:
                return 0 # In the range
        
        def binarySearch(arr, t):
            l = 0
            h = len(arr) - 1

            while(l<=h):
                mid = (l+h)//2
                if(t==arr[mid]):
                    return True
                elif (t<arr[mid]):
                    h = mid - 1
                else:
                    l = mid + 1
            
            return False
        
        l = 0
        h = len(matrix) - 1

        while(l<=h):
            mid = (l+h)//2
            check = isCorrect(mid)

            if(check==0):
                return binarySearch(matrix[mid], target)
            elif(check==-1):
                h = mid - 1
            else:
                l = mid + 1
        return False
                
        