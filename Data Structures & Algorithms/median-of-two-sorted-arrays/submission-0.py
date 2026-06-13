class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Calculate Total, Half
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            midA = (left + right) // 2
            midB = half - midA - 2

            ALeft = A[midA] if midA >= 0 else float('-infinity')
            ARight = A[midA+1] if (midA + 1) <len(A) else float('infinity')

            BLeft = B[midB] if midB >= 0 else float('-infinity')
            BRight = B[midB + 1] if (midB+1) < len(B) else float('infinity')

            # Partition is sorted

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2

            elif ALeft > BRight:
                right = midA - 1
            
            else:
                left = midA + 1

