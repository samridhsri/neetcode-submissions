class Solution {
    public boolean isPalindrome(String s) {

        int i = 0;
        int j = s.length() - 1;

        while ( i < j){
            if (i < j && !Character.isLetterOrDigit(s.charAt(i))){
                i++;
                continue;
            }

            if (i < j && !Character.isLetterOrDigit(s.charAt(j))){
                j--;
                continue;
            }

            if(s.toLowerCase().charAt(i)!=s.toLowerCase().charAt(j)){
                return false;
            }

            i++;
            j--;
        }

        return true;
        
    }
}
