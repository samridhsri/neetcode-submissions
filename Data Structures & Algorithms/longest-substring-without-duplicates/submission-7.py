class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [False] * 128

        left = 0
        result = 0

        for right in range(left, len(s)):
            while seen[ord(s[right]) - ord('a')]:
                seen[ord(s[left]) - ord('a')] = False
                left+=1
            
            seen[ord(s[right]) - ord('a')] = True
            result = max(result, right - left + 1)
        
        return result