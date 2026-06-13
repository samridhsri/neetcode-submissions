class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = [False] * 128
        left = 0
        res = 0

        for right in range(len(s)):

            while(seen[ord(s[right])]):
                seen[ord(s[left])] = False
                left += 1

            seen[ord(s[right])] = True
            res = max(res, right - left + 1)
        
        return res