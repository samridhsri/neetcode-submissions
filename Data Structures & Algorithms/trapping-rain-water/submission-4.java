class Solution {
    // Two Pointer
    public int trap(int[] height) {
        int l = 0;
        int r = height.length-1;

        int leftMax = height[0];
        int rightMax = height[r];

        int res = 0;
    

        while(l < r){
            if(height[l] < height[r]){
                if(height[l] >= leftMax) {
                leftMax = height[l];
                }

                else {
                res += leftMax - height[l];
                }

                l++;    
            }

            else{
                if(height[r] >= rightMax){
                    rightMax = height[r];
                }
                else{
                    res+=rightMax - height[r];
                }

                r--;
            }


        }

        return res;
    }
}
