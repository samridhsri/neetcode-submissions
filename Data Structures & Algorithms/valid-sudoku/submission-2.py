class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        column = {}
        rows = {}
        square = {}


        for row in range(0,9):
            for col in range(0,9):

                val = board[row][col]

                if val == ".":
                    continue
                
                if col not in column:
                    column[col] = set()
                
                if row not in rows:
                    rows[row] = set()
                
                if (row//3, col//3) not in square:
                    square[(row//3, col//3)] = set()
                
                if val in rows[row] or val in column[col] or val in square[(row//3, col//3)]:
                    return False
                
                rows[row].add(val)
                column[col].add(val)
                square[(row//3, col//3)].add(val)
        
        return True