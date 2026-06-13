class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        countToWord = {}

        for stri in strs:
            count = [0] * 26

            for ch in stri:
                count[ord(ch) - ord('a')] += 1
            
            countToWord[tuple(count)] = countToWord.get(tuple(count),[])
            countToWord[tuple(count)].append(stri)
        
        result = []
        for key, values in countToWord.items():
            result.append(values)
        
        return result