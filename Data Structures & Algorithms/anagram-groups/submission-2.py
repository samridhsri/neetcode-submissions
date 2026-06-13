class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqGlobal = {}

        for word in strs:
            
            count = [0]*26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            if tuple(count) not in freqGlobal:
                freqGlobal[tuple(count)] = []
            
            freqGlobal[tuple(count)].append(word)
        
        result = []

        for key in freqGlobal:
            result.append(freqGlobal[key])
        
        return result