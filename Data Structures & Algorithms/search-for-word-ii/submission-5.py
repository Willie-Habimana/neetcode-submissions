class Node:

    def __init__(self, char = None):
        self.char = char
        self.children = {}
        self.EOW = None



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.ans = []
        self.root = Node()

        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node(c)
                curr = curr.children[c]
            curr.EOW = word

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char in self.root.children:
                    self.dfs(i,j,self.root.children[char], set([(i,j)]))
        
        return list(set(self.ans))
        


    def dfs(self, r, c, node, seen):
        if node.EOW:
            self.ans.append(node.EOW)
        if len(node.children) == 0:
            return
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for d in directions:
            row = r + d[0]
            col = c + d[1]
            if ((row, col) not in seen and self.isValid(row, col)
                and self.board[row][col] in node.children):
                seen.add((row,col))
                self.dfs(row, col, node.children[self.board[row][col]], seen)
                seen.remove((row,col))


    def isValid(self, r, c):
        return r >= 0 and c >= 0 and r < len(self.board) and c < len(self.board[0])


        