class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}

        for ch in s:
           freq_s[ch] = freq_s.get(ch, 0) + 1

        for ch in t:
            if ch not in freq_s:
                return False
            
            if freq_s[ch] == 0:
                return False
            
            freq_s[ch] = freq_s[ch] - 1
        
        for k in freq_s:
            if freq_s[k] != 0:
                return False
        
        return True