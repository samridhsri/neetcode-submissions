class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitsToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def helper(i, curCombination):
            if len(curCombination) == len(digits):
                res.append(curCombination)
                return
            
            #Include and exclude
            for ch in digitsToLetter[digits[i]]:
                helper(i+1, curCombination + ch)
        
        if digits:
            helper(0, "")
        return res