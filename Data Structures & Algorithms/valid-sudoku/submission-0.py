class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = {}
        rows = {}
        squares = {}

        for r in range(0,9):
            for c in range(0,9):

                val = board[r][c]

                if val == ".":
                    continue
                
                # Created the keys in each dictionary
                
                if c not in cols:
                    cols[c] = set()
                
                if r not in rows:
                    rows[r] = set()
                
                if (r//3, c//3) not in squares:
                    squares[(r//3, c//3)] = set()
                
                # Check for the conditions

                # Check in row, column and square
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)
        
        return True
