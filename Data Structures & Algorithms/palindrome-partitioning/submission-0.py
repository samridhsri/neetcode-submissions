class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        partition = []

        def helper(i):
            # This function is going to help me partition the string

            if i >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    helper(j+1)
                    partition.pop()
            
        helper(0)
        return result
    
    def isPalindrome(self, s, i, j):
        l, r = i, j
        while l < r:
            if s[l] != s[r]:
                return False
            
            l, r = l+1, r-1
        return True