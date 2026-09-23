class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int maxK = 0;

        for(int pile : piles){
            maxK = Math.max(pile, maxK);
        }

        int l = 1;
        int r = maxK;
        int res = maxK;

        while(l <= r){
            long hour = 0;
            int k = l + (r - l) / 2;

            for(int pile : piles){
                hour = hour + (pile + k - 1)/k;
            }

            if(hour <= h){
                // this works, search for more;
                r = k - 1;
                res = k;
            }
            else if(hour > h){
                l = k + 1;
            }
        }

        return res;
    }
}
