class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.ans = []
        self.board = [['.' for _ in range(n)] for _ in range(n)]

        self.dfs(0)

        return self.ans

    def dfs(self, i):
        if i == self.n:
            self.ans.append(["".join(l) for l in self.board])
            return
        
        for j in range(self.n):
            if self.check(i,j):
                self.board[i][j] = 'Q'
                self.dfs(i+1)
                self.board[i][j] = '.'

    

    def check(self, r,c):
        diagonals = [(-1,1), (-1,-1)]
        for d in diagonals:
            row = r + d[0]
            col = c + d[1]
            while row >= 0 and col >= 0 and col < self.n:
                if self.board[row][col] == 'Q':
                    return False
                row += d[0]
                col += d[1]


        for i in range(0, r):
            if self.board[i][c] == 'Q':
                return False
        
        return True
            


        




        