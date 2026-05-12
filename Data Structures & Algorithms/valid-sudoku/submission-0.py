class Solution:
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkColumns(board) and self.checkRows(board) and self.checkSquares(board)


    def checkColumns(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != "." \
                and (board[j][i] in seen 
                or board[j][i] not in self.numbers):
                    return False
                seen.add(board[j][i])
        
        return True


    def checkRows(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != "." \
                and (board[i][j] in seen 
                or board[i][j] not in self.numbers):
                    return False
                seen.add(board[i][j])
        
        return True


    def checkSquares(self, board):
        starting_points = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for sp in starting_points:
            seen = set()
            for i in range(3):
                for j in range(3):
                    cell = board[i+sp[0]][j+sp[1]]
                    if cell != "." \
                    and (cell in seen 
                    or cell not in self.numbers):
                        return False
                    seen.add(cell)
        
        return True
                    



        