class Solution {
    public int findMin(int[] nums) {
        int min = nums[0];
        int size = nums.length - 1;

        if(nums[0] < nums[size]){
            return nums[0];
        }

        else{
            int l = 0;
            int r = size;

            while(l <= r){
                int mid = l + (r - l) / 2;
                min = Math.min(nums[mid], min);

                if (nums[mid] < nums[r]){
                    r = mid - 1;
                }
                else{
                    l = mid + 1;
                }
            }

            return min;
        }
    }
}
