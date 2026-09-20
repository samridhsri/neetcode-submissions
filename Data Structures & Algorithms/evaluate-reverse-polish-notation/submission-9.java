class Solution {
    public int evalRPN(String[] tokens) {
        
        Stack<Integer> stack = new Stack<>();

        for(String num : tokens){
            if(num.equals("+")){
                int a = stack.pop();
                int b = stack.pop();

                stack.push(a+b);
            }

            else if(num.equals("-")){
                int a = stack.pop();
                int b = stack.pop();

                stack.push(b-a);
            }

            else if(num.equals("*")){
                int a = stack.pop();
                int b = stack.pop();

                stack.push(a*b);
            }

            else if(num.equals("/")){
                int a = stack.pop();
                int b = stack.pop();

                stack.push(b/a);
            }

            else{
                stack.push(Integer.parseInt(num));
            }
        }

        return stack.pop();
    }
}
