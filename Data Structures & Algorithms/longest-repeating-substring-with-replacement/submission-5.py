class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        freqMap = {}
        result = 0
        maxFreqInsideWindow = 0

        for right in range(len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            maxFreqInsideWindow = max(freqMap[s[right]], maxFreqInsideWindow)

            windowLength = right - left + 1

            while (windowLength - maxFreqInsideWindow) > k:
                freqMap[s[left]] = freqMap[s[left]] - 1
                left += 1
                windowLength = right - left + 1
            
            result = max(result, right-left+1)
        
        return result