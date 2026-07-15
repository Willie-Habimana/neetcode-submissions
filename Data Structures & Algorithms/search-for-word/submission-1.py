class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.visited = set()
        self.word = word
        self.directions = [(1,0), (-1,0), (0,-1), (0,1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.visited.add((i,j))
                    if self.helper(i,j,1):
                        return True
                    self.visited.remove((i,j))
        
        return False
    


    def isValid(self, r, c):
        rows = len(self.board)
        cols = len(self.board[0])
        if r >= 0 and c >= 0 and r < rows and c < cols:
            return True
        else:
            return False
    
    def helper(self, r, c, i):
        if i == len(self.word):
            return True
        
        for d in self.directions:
            _r = r + d[0]
            _c = c + d[1]
            if self.isValid(_r, _c) and self.board[_r][_c] == self.word[i] and (_r, _c) not in self.visited:
                self.visited.add((_r, _c))
                if self.helper(_r, _c, i+1) == True:
                    return True
                self.visited.remove((_r, _c))
        
        return False
        







        