class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}

        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        
        for ch in t:
            if ch not in freq_s:
                return False
            
            freq_s[ch] = freq_s[ch] - 1
        
        for value in freq_s.values():
            if value != 0:
                return False
        
        return True