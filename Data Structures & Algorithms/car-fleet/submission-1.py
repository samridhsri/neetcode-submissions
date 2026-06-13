class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        positionAndSpeed = []

        for i in range(len(position)):
            positionAndSpeed.append((position[i], speed[i]))
        
        positionAndSpeed = sorted(positionAndSpeed, key = lambda x: x[0])

        stack = []

        for i in range(len(position)-1, -1, -1):

            timeToReach = (target - positionAndSpeed[i][0]) / positionAndSpeed[i][1]

            stack.append(timeToReach)

            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return len(stack)