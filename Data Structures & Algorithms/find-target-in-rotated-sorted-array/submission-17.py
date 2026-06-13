class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search

        def binarySearch(l, r, target):
            while(l<=r):
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    l = mid + 1
                
                else:
                    r = mid - 1
            return -1
        
        # Find the pivot: Index of the smallest element

        l, r = 0, len(nums)-1
        while(l<r):
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid+1
            
            else:
                r = mid
        
        pivot = l

        a = binarySearch(0, pivot-1, target)
        b = binarySearch(pivot, len(nums)-1, target)

        return a if a!=-1 else b

        