class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                curr = stack.pop()
                curr_index = curr[1]
                res[curr_index] = i - curr_index
            
            temp = (n,i)
            stack.append(temp)
            
        return res
                