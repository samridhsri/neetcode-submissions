class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        tupleToString = {}

        for stri in strs:
            count = [0] * 26

            for ch in stri:
                count[ord(ch) - ord('a')] += 1
            tupleToString[tuple(count)] = tupleToString.get(tuple(count), [])
            tupleToString[tuple(count)].append(stri)

        for key, values in tupleToString.items():
            result.append(tupleToString[key])
        return result 

