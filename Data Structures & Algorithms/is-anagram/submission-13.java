class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()){
            return false;
        }

        int[] freq = new int[26];

        for(char ch : s.toCharArray()){
            freq[ch - 'a'] += 1;
        }

        for(char ch : t.toCharArray()){
            freq[ch - 'a'] -= 1;
        }

        for(int i : freq){
            if (i!=0) return false;
        }

        return true;

    }
}
