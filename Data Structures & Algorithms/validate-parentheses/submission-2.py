class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')' : '(',  ']' : '[', '}' : '{'  }
        stack = []
        
        for c in s:
            if (c not in dictionary):
                stack.append(c)
                continue
            if not stack or stack[-1] != dictionary[c]:
                return False
            stack.pop()
        
        return not stack
            
                

            
