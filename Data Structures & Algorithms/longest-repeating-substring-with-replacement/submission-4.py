class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        windowFreqMap = {}
        left = 0
        res = 0
        maxFreqInsideWindow = 0

        for right in range(len(s)):
            windowFreqMap[s[right]] = 1 + windowFreqMap.get(s[right], 0)
            
            windowLength = right - left + 1
            maxFreqInsideWindow = max(maxFreqInsideWindow, windowFreqMap[s[right]])

            while((windowLength - maxFreqInsideWindow) > k):
                windowFreqMap[s[left]] -= 1
                left += 1
                windowLength = right - left + 1
            
            res = max(res, right - left + 1)
        
        return res

