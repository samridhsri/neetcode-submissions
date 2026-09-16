class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;

        while(i < j && (i < numbers.length) && (j > -1)){
            int calculate = numbers[i] + numbers[j];

            if(calculate == target){
                return new int[] {i+1, j+1};
            }

            else if(calculate < target){
                i++;
            }

            else{
                j--;
            }
        }

        return new int[] {-1, -1};
    }
}
