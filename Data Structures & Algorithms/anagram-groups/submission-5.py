class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        anagrams = {}

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            anagrams[tuple(count)] = anagrams.get(tuple(count), [])
            anagrams[tuple(count)].append(s)
        
        for k, v in anagrams.items():
            result.append(anagrams[k])
        return result