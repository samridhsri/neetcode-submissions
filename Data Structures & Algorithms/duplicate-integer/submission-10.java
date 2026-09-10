class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> checkDuplicate = new HashSet<>();

        for(int x: nums){
            if(checkDuplicate.contains(x)){
                return true;
            }

            checkDuplicate.add(x);
        }

        return false;
    }
}