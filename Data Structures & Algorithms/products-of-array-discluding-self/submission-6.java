class Solution {
    public int[] productExceptSelf(int[] nums) {

        int size = nums.length;

        int[] pre = new int[size];
        int[] post = new int[size];

        int[] res = new int[size];


        pre[0] = 1;
        post[size-1] = 1;

        for(int i = 1; i < size; i++){
            pre[i] = pre[i-1]*nums[i-1];
        }

        for(int i = size-2; i>=0; i--){
            post[i] = post[i+1] * nums[i+1];
        }

        for(int i = 0; i<size; i++){
            res[i] = pre[i] * post[i];
        }

        return res;
    }
}  
