class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Easy: Use Dictionary

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in t:
            if ch in freq:
                freq[ch] -= 1
            else:
                return False
        
        for key in freq:
            if freq[key]!=0:
                return False
        return True