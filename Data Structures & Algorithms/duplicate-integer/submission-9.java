class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checkDuplicate = new HashSet<>();

        for(int i=0; i<nums.length; i++){
            if (checkDuplicate.contains(nums[i])){
                return true;
            }

            checkDuplicate.add(nums[i]);
        }

        return false;


    }
}