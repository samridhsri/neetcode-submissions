class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;

        List<List<Integer>> buckets = new ArrayList<>();

        for(int i=0; i<=n; i++){
            buckets.add(new ArrayList<>());
        }

        // Calculate the frequency Map for each digit

        HashMap<Integer, Integer> numToFreq = new HashMap<>();

        for(int num : nums){
            numToFreq.put(num, numToFreq.getOrDefault(num, 0)+1);
        }

        // We are ready with our freq Map
        
        // Add them to buckets

        for(Map.Entry<Integer, Integer> entry : numToFreq.entrySet()){
            int number = entry.getKey();
            int bucket = entry.getValue();

            buckets.get(bucket).add(number);
        }

        // We are ready with buckets now
        // create a result array that we can return in the end

        int[] res = new int[k];

        int index = 0;

        for(int i = buckets.size()-1; i>0 && index<k; i--){
            if(buckets.get(i).isEmpty()) continue;

            for(int num: buckets.get(i)){
                res[index] = num;
                index++;

                if(index==k || index>k){
                    return res;
                }
            }
        }

        return res;
    }
}
