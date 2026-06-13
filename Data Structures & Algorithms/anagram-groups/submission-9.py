class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Make a dictionary with array freq -> anagram array

        freqToAnagram = {}

        for word in strs:
            arr = [0] * 26

            for ch in word:
                arr[ord(ch)-ord('a')] += 1
            
            if tuple(arr) not in freqToAnagram:
                freqToAnagram[tuple(arr)] = []
            
            freqToAnagram[tuple(arr)].append(word)
        
        result = []
        for key, value in freqToAnagram.items():
            result.append(value)
        
        return result
