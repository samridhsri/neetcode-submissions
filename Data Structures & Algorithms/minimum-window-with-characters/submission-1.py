class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        res, resLen = [-1, -1], float("infinity")

        counter_t, window = {}, {}

        for ch in t:
            counter_t[ch] = counter_t.get(ch, 0) + 1
        
        have, need = 0, len(counter_t)

        left = 0

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in counter_t and window[ch] == counter_t[ch]:
                have+=1
            

            while have == need:
                windowLength = (right - left) + 1

                if windowLength < resLen:
                    resLen = windowLength
                    res = [left, right]
                
                window[s[left]] -= 1
                if s[left] in counter_t and window[s[left]] < counter_t[s[left]]:
                    have -= 1
                
                left += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""