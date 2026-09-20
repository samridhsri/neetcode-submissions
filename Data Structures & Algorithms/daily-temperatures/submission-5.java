class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int size = temperatures.length;

        int[] res = new int[size];

        for(int i = 0; i < size; i++){
            while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]){
                int stackIndex = stack.pop();
                res[stackIndex] = i - stackIndex;
                
            }
            stack.push(i);
        }

        return res;
    }
}
