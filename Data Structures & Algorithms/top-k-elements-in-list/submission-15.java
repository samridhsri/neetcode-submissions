class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int n = nums.length;

        ArrayList<Integer>[] buckets = new ArrayList[n+1];
        HashMap<Integer, Integer> freq = new HashMap<>();

        for(int num: nums){
            freq.put(num, freq.getOrDefault(num, 0)+1);
        }

        for(Map.Entry<Integer,Integer> entry : freq.entrySet()){
            int num = entry.getKey();
            int count = entry.getValue();

            if (buckets[count]==null){
                buckets[count] = new ArrayList<>();
            }

            buckets[count].add(num);
        }

        int[] results = new int[k];
        int index = 0;

        for(int i=n; i>=0 && index < k; i--){
            if(buckets[i] != null){
                for(int num : buckets[i]){
                    results[index] = num;
                    index++;
                }
            }
        }

        return results;
        
    }
}
