class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, word[1:], set([(i,j)])):
                        return True
        
        return False
    


    def dfs(self, r, c, board, word, seen):
        if len(word) == 0:
            return True
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for d in directions:
            row = r + d[0]
            col = c + d[1]
            if ((row,col) not in seen 
                and self.isValid(row, col, len(board), len(board[0])) 
                and board[row][col] == word[0]):
                seen.add((row, col))
                if self.dfs(row, col, board, word[1:], seen):
                    return True
                seen.remove((row,col))
        return False
        
    def isValid(self, row, col, m, n):
        return row >= 0 and col >=0 and row < m and col < n








        