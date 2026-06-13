class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        left = 0

        if len(s) < 2:
            return len(s)
        
        seen = [False] * 128

        for right in range(len(s)):
            while seen[ord(s[right])]:
                seen[ord(s[left])] = False
                left+=1
            
            seen[ord(s[right])] = True
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength