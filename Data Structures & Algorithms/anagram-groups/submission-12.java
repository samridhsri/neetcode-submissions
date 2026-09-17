class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> freqToString = new HashMap<>();

        for(String str: strs){
            int[] freq = new int[26];

            for(char ch : str.toCharArray()){
                freq[ch - 'a']++;
            }

            String key = Arrays.toString(freq);

            List<String> temp = freqToString.getOrDefault(key, new ArrayList<String>());

            temp.add(str);

            freqToString.put(key,temp);
        }


        return new ArrayList<>(freqToString.values());
    }
}
