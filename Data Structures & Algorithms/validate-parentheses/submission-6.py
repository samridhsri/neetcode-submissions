class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(',']':'[','}':'{'}
        stack = []
        top = 0
        if len(s)<=1:
            return False
        for st in s:
            if st in closeToOpen:
                if(len(stack)==0):
                    return False
                # check top
                if(stack[top] == closeToOpen.get(st)):
                    stack.pop()
                    top = len(stack) - 1
                else:
                    return False
                
            if st=='(' or st=='[' or st=='{':
                stack.append(st)
                top = len(stack) - 1
        
        if len(stack) == 0:
            return True
        else:
            return False