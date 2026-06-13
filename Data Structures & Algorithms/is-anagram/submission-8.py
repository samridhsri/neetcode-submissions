class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False

        alpha = [0] * 26

        for ch in s:
            alpha[ord(ch) - ord('a')] += 1
        
        for ch in t:
            alpha[ord(ch) - ord('a')] -= 1
        
        for ch in alpha:
            if ch!=0:
                return False
        
        return True