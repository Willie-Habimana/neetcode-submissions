class Node:
    def __init__(self, word: str = None):
        self.word = word
        self.children = {}
        self.EOW = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = set()
        sources = {}
        seen = set()
        curr_word = []
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r,c, node):
            if node.EOW == True:
                ans.add("".join(curr_word))

            if len(node.children) == 0:
                return

            for d in directions:
                row = r + d[0]
                col = c + d[1]

                if (row >= 0 and col >= 0 and row < len(board) and col < len(board[0])
                    and (row, col) not in seen and board[row][col] in node.children):
                    seen.add((row,col))
                    curr_word.append(board[row][col])
                    dfs(row, col, node.children[board[row][col]])
                    seen.remove((row,col))
                    curr_word.pop()
            
        
        for word in words:
            curr = sources[word[0]] if word[0] in sources else Node(word)
            if word[0] not in sources:
                sources[word[0]] = curr 
            for i in range(1, len(word)):
                if word[i] in curr.children:
                    curr = curr.children[word[i]]
                else:
                    new_node = Node(word)
                    curr.children[word[i]] = new_node
                    curr = new_node
            curr.EOW = True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in sources:
                    seen.add((i,j))
                    curr_word.append(board[i][j])
                    dfs(i,j, sources[board[i][j]])
                    seen.remove((i,j))
                    curr_word.pop()
        
        return list(ans)
        

        
        
        


        