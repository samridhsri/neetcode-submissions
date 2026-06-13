class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                t, i = stack.pop()
                res[i] = index - i
            stack.append([temp, index])
        return res

        # Subtract current values index with the index of the popped element