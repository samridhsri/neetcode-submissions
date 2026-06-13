class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        #check with HashSet

        map_s = {}
        map_t = {}

        for char in s:
            freq = map_s.get(char, 0)
            map_s[char] = freq + 1
        
        for char in t:
            freq = map_t.get(char, 0)
            map_t[char] = freq + 1
        
        if(map_t==map_s):
            return True
        else:
            return False
            