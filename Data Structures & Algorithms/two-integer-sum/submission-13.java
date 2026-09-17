class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int toFind = target - nums[i];

            if (numToIndex.containsKey(toFind)){
                if (i < numToIndex.get(toFind)) {
                    return new int[] {i, numToIndex.get(toFind)};
                }
                else{
                    return new int[] {numToIndex.get(toFind), i};
                }
            }

            numToIndex.put(nums[i], i);
        }

        return new int[] {-1, -1};
    }
}
