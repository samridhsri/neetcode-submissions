class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Sort the array based on Position

        positionAndSpeed = []
        n = len(position)

        for i in range(n):
            positionAndSpeed.append((position[i],speed[i]))
        
        positionAndSpeed = sorted(positionAndSpeed, key = lambda x: x[0])

        # Create stack and iterate through positionAndSpeed from right to left
        stack = []

        for i in range(n-1, -1, -1):
            # Calculate Time to Reach
            timeToReach = (target - positionAndSpeed[i][0]) / positionAndSpeed[i][1]
            stack.append(timeToReach)
            if len(stack) >=2 and stack[-1] <= stack[-2]: # jo abhi add hua woh pehle wale se bada ho
                stack.pop()
        
        return len(stack)


