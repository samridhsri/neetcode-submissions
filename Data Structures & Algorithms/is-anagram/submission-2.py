class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Anagrams -> both words have same frequency of letters

        # Use dictionary

        freq = {}

        if len(s)!=len(t):
            return False
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in t:
            if ch not in freq:
                return False
            
            freq[ch] = freq.get(ch) - 1
        
        for key in freq.keys():
            if freq[key]!=0:
                return False
        
        return True