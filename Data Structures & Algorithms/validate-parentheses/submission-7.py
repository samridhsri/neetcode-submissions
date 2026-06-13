class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        para = {
            ')':'(',
            '}': '{',
            ']' : '[',
        }

        for char in s:
            if char in para:
                if not stack or stack[-1]!=para[char]:
                    return False
                stack.pop()
            
            else:
                stack.append(char)
        
        return len(stack)==0

