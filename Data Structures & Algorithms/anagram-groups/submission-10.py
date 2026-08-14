class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqToStr = {}
        for string in strs:
            chars = [0] * 26

            for ch in string:
                ch = ch.lower()
                chars[ord(ch) - ord('a')] += 1
            
            if tuple(chars) not in freqToStr:
                freqToStr[tuple(chars)] = []
            
            freqToStr[tuple(chars)].append(string)
        
        result = []

        for item in freqToStr.values():
            result.append(item)
        
        return result