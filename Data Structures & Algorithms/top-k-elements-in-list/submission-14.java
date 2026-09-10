class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        int n = nums.length;

        ArrayList<Integer>[] buckets = new ArrayList[n+1];

        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for(int num: nums){

            freqMap.put(num, freqMap.getOrDefault(num, 0)+1);
        }

        for(Map.Entry<Integer, Integer> entry: freqMap.entrySet()){

 int num = entry.getKey();
            int freq = entry.getValue();

            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }

            buckets[freq].add(num);        }

        int[] result = new int[k];
        int index = 0;

        for(int i=n; i>=0 && index < k; i--){
            if (buckets[i]!=null){
                for(int num : buckets[i]){
                    result[index] = num;
                    index++;
                }
            }
        }

        return result;


    }
}
