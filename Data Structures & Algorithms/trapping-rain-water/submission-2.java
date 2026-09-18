class Solution {
    public int trap(int[] height) {
        int size = height.length;
        int[] rightLargest = new int[size];
        int[] leftLargest = new int[size];

        leftLargest[0] = height[0];


        for(int i = 1; i < size; i++){
            leftLargest[i] = Math.max(leftLargest[i-1],height[i]);
        }

        rightLargest[size-1] = height[size-1];

        for(int i = size-2; i>=0; i--){
            rightLargest[i] = Math.max(rightLargest[i+1], height[i]);
        }

        int res = 0;

        for(int i = 0; i < size; i++){
            res = res + Math.min(leftLargest[i], rightLargest[i]) - height[i];
        }

        return res;

    }
}
