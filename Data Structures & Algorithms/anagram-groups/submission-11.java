class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<List<Integer>,ArrayList<String>> freqMap = new HashMap<>();

        for(String str : strs){

            int[] freq = new int[26];

            for(char ch : str.toCharArray()){
                freq[ch - 'a']++;
            }

            List<Integer> key = new ArrayList<>();

            for(int count : freq){
                key.add(count);
            }

            freqMap.putIfAbsent(key, new ArrayList<>());
            freqMap.get(key).add(str);

        }

        return new ArrayList<>(freqMap.values());
    }
}
