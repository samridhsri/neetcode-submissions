class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int size = position.length;

        Integer[] indices = new Integer[size];

        for(int i = 0; i<size; i++){
            indices[i] = i;
        }

        int[] sortedPosition = new int[size];
        int[] sortedSpeed = new int[size];

        Arrays.sort(indices, (a,b) -> Integer.compare(position[a],position[b]));

        for(int i = 0; i < size; i++){
            sortedPosition[i] = position[indices[i]];
            sortedSpeed[i] = speed[indices[i]];
        }

        double[] time = new double[size];

        for(int i=0; i<size; i++){
            time[i] = (double)(target - sortedPosition[i]) / sortedSpeed[i];
        }

        Stack<Double> stack = new Stack<>();

        for(int i = size-1; i >= 0; i--){
            if((stack.isEmpty()) || (time[i] > stack.peek())){
                stack.push(time[i]);
            }
        }

        return stack.size();



    }
}
