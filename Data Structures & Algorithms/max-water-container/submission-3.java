class Solution {
    public int maxArea(int[] heights) {

        int l = 0;
        int r = heights.length - 1;

        int maxWater = 0;

        while(l<r){
            int calculate = Math.min(heights[l], heights[r]) * (r-l);

            if(heights[l] < heights[r]){
                l++;
            }

            else{
                r--;
            }

        maxWater = Math.max(calculate, maxWater);
        }

        return maxWater;

        
    }
}
