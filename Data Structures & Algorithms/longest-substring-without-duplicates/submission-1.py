class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Boolean Array method

        seen = [False] * 128
        l = 0
        res = 0

        for r in range(len(s)):

            while seen[ord(s[r])]:
                seen[ord(s[l])] = False
                l+=1
            
            seen[ord(s[r])] = True
            res = max(res, r-l+1)
        
        return res