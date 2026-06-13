class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<2:
            return len(s)
        
        check = set()

        r = 0
        l = 0
        res = 0
        while r<len(s):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            
            check.add(s[r])
            r+=1

            res = max(res, r-l)
        
        return res