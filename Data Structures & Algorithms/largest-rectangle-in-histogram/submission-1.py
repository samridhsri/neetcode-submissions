class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Idea is to keep on adding elements to stack while the next height is greater
        
        maxArea = 0
        stack = []

        for index, height in enumerate(heights):
            start = index # start keeps track of the starting index
            while stack and stack[-1][1] > height:
                curr_index, curr_height = stack.pop()
                maxArea = max(maxArea, curr_height*(index - curr_index))
                start = curr_index
            
            stack.append((start, height))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea