class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, j):
            stack = []
            stack.append((i,j))
            seen = set()
            surrounded = True
            while stack:
                node = stack.pop()
                seen.add(node)
                visited.add(node)
                for d in directions:
                    r = node[0] + d[0]
                    c = node[1] + d[1]
                    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                        surrounded = False
                    elif (r,c) not in seen and board[r][c] == 'O':
                        stack.append((r,c))
            
            return seen if surrounded else None
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j] == 'O':
                    surr = dfs(i,j)
                    if surr:
                        for node in surr:
                            board[node[0]][node[1]] = 'X'
        

            
            
                        



        