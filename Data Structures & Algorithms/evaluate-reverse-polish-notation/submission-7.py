class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for num in tokens:

            match num:
                case '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(a)+int(b)))
                
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(b)-int(a)))
                
                case '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(a)*int(b)))
                
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(int(b) / int(a))))
                
                case _:
                    stack.append(num)
        return int(stack[-1])