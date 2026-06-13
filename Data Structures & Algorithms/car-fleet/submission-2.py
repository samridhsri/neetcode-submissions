class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # The idea is to calculate time then compare on the basis of time to reach
        # Agar kam time lag raha hai toh pop in the stack

        n = len(position)

        positionAndSpeed = []
        stack = []

        for i in range(n):
            positionAndSpeed.append((position[i], speed[i]))
        
        positionAndSpeed = sorted(positionAndSpeed, key = lambda x : x[0])

        for i in range(n-1, -1, -1):
             # Calculate the time to reach for every car on the basis of position

             timeToReach = (target - positionAndSpeed[i][0]) / positionAndSpeed[i][1]

             stack.append(timeToReach)

             if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
