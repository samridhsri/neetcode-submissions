class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        countToList = {}

        for str in strs:

            count = [0] * 26

            for ch in str:
                count[ord(ch) - ord('a')] += 1
            
            countToList[tuple(count)] = countToList.get(tuple(count), [])
            countToList[tuple(count)].append(str)
        
        result = []
        for key, value in countToList.items():
            result.append(value)
        
        return result