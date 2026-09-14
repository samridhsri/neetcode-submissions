class Solution {
    public boolean isPalindrome(String s) {

        int i = 0;
        int j = s.length() - 1;

        while(i < j){

            while(i<j && !Character.isLetterOrDigit(s.charAt(i))){
                i++;
                continue;
            }

            while(i<j && !Character.isLetterOrDigit(s.charAt(j))){
                j--;
                continue;
            }

            char firstLetter = s.toLowerCase().charAt(i);
            char lastLetter = s.toLowerCase().charAt(j);

            if(firstLetter != lastLetter){
                return false;
            }

            i++;
            j--;
        }

        return true;
        
    }
}
