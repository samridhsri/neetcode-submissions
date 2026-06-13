class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtracking(perm: List[int], used: List[bool]):

            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if(not used[i]):
                    used[i] = True
                    perm.append(nums[i])
                    backtracking(perm, used)
                    perm.pop()
                    used[i] = False
        
        backtracking([], [False] * len(nums))
        return result