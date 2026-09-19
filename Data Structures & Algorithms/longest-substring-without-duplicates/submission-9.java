class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int maxL = 0;

        HashSet<Character> checkDuplicate = new HashSet<>();

        for(int r = 0; r < s.length(); r++){
            if(checkDuplicate.contains(s.charAt(r))){
                while((checkDuplicate.contains(s.charAt(r))) && (l < r)){
                    checkDuplicate.remove(s.charAt(l));
                    l++;
                }
            }

            checkDuplicate.add(s.charAt(r));

            maxL = Math.max(maxL, r - l + 1);

        }

        return maxL;
    }
}
