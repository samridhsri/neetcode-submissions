class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        para = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:
            if ch in para:
                if not stack or stack[-1]!=para[ch]:
                    return False
                stack.pop()
            
            else:
                stack.append(ch)
        
        return len(stack)==0

    


# ({Stack}) -> [ (, { ]