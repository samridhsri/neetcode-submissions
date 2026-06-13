class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if count_s1[i] == count_s2[i]:
                matches += 1
            
            
        
        left = 0

        for right in range(len(s1), len(s2)):

            if matches == 26:
                return True

            count_s2[ord(s2[right]) - ord('a')] += 1

            if count_s2[ord(s2[right]) - ord('a')] == count_s1[ord(s2[right]) - ord('a')]:
                matches += 1
            
            elif count_s2[ord(s2[right]) - ord('a')] - 1 == count_s1[ord(s2[right]) - ord('a')]:
                matches -= 1
            
            count_s2[ord(s2[left]) - ord('a')] -= 1

            if count_s2[ord(s2[left]) - ord('a')] == count_s1[ord(s2[left]) - ord('a')]:
                matches += 1
            
            elif count_s2[ord(s2[left]) - ord('a')] + 1 == count_s1[ord(s2[left]) - ord('a')]:
                matches -= 1
            
            left += 1
        
        return matches == 26