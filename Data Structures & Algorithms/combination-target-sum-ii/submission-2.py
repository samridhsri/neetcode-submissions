class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        curSet = []

        def helper(i, curSum):
            if curSum == target:
                result.append(curSet.copy())
                return
            
            if curSum > target or i >= len(candidates):
                return
            
            curSet.append(candidates[i])
            helper(i+1, curSum + candidates[i])

            curSet.pop()

            while(i+1 < len(candidates) and candidates[i]==candidates[i+1]):
                i+=1

            helper(i+1, curSum)
        
        helper(0,0)
        return result
        