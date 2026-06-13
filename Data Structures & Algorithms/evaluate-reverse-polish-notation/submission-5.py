class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for num in tokens:
            match num:
                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    res = int(a) + int(b)
                    stack.append(str(res))
                
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    res = int(a) - int(b)
                    stack.append(str(res))
                
                case "*":
                    b = stack.pop()
                    a = stack.pop()
                    res = int(a) * int(b)
                    stack.append(str(res))
                
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    res = int(int(a) / int(b))
                    stack.append(str(res))
                
                case _:
                    stack.append(num)
            
        return int(stack[-1])