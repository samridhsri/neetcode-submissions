class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqMap = {}

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            
            freqMap[tuple(count)] = freqMap.get(tuple(count), [])
            freqMap[tuple(count)].append(word)
        
        result = []

        for key in freqMap:
            result.append(freqMap[key])
        
        return result
