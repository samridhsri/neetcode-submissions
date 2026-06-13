class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        columns = {}
        rows = {}
        square = {}

        for row in range(0,9):
            for column in range(0,9):

                val = board[row][column]

                if val == ".":
                    continue
                
                if row not in rows:
                    rows[row] = set()
                
                if column not in columns:
                    columns[column] = set()
                
                if (row//3, column//3) not in square:
                    square[(row//3, column//3)] = set()
                
                if val in rows[row] or val in columns[column] or val in square[(row//3, column//3)]:
                    return False
                
                rows[row].add(val)
                columns[column].add(val)
                square[(row//3, column//3)].add(val)
        
        return True