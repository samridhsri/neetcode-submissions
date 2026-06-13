class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            # Idea is to pop from stack until we find something bigger

            while stack and num > stack[-1][0]:
                curr = stack.pop()
                curr_index = curr[1]
                res[curr_index] = index - curr_index
            
            stack.append((num, index))
        
        return res