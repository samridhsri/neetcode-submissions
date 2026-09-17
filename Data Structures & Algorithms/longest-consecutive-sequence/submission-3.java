class Solution {
    public int longestConsecutive(int[] nums) {

        // Lets make a HashSet first

        HashSet<Integer> numsMap = new HashSet<>();

        for(int num : nums){
            numsMap.add(num);
        }

        int maxStreak = 0;

        for(int num : nums){
            if(!numsMap.contains(num-1)){
                int length = 1;
                int curr = num;

                while(numsMap.contains(curr+1)){
                    curr = curr+1;
                    length+=1;
                }

                maxStreak = Math.max(maxStreak, length);
            }
        }

        return maxStreak;
        
    }
}
