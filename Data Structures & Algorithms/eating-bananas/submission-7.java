class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int maxK = 0;

        for(int pile : piles){
            maxK = Math.max(pile, maxK);
        }

        int l = 1;
        int r = maxK;
        int res = 0;

        while(l <= r){
            int k = (l + (r - l) / 2);

            long hour = 0;

            for(int pile : piles){
                hour = hour + ((pile + k - 1) / k);
            }

            if(hour <= h){
                // this works
                res = k;
                r = k - 1;
            }

            else if(hour > h){
                    l = k + 1;
                }

            

        }

        return res;
    }
}
