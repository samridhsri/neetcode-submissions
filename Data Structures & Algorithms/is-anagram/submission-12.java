class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        int[] freq = new int[26];

        for(char ch : s.toCharArray()){
            ch = Character.toLowerCase(ch);
            freq[ch - 'a']++;
        }

        for(char ch : t.toCharArray()){
            ch = Character.toLowerCase(ch);
            freq[ch - 'a']--;
        }

        for(int x : freq){
            if (x!=0){
                return false;
            }
        }

        return true;

    }
}
