class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for ch in s:
            if ch in closeToOpen:
                if stack and closeToOpen[ch] == stack[-1]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(ch)
        
        return len(stack) == 0