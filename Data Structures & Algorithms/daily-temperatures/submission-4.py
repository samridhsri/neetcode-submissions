class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # make a stack
        stack = []
        res = [0] * len(temperatures)

        for index, num in enumerate(temperatures):

            while stack and num > stack[-1][0]:
                curr = stack.pop()
                curr_index = curr[1]
                res[curr_index] = index - curr_index
            
            stack.append((num, index))
        
        return res