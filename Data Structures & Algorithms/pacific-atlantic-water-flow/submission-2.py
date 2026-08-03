class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        bool_list = [[{'p': False, 'a': False} for _ in range(len(heights[0]))] for _ in range(len(heights))]
        print(len(bool_list))
        print(bool_list[0])
        p_q = deque()
        a_q = deque()
        for i in range(len(heights[0])):
            p_q.append((0, i, 'p'))
            a_q.append((len(heights) -1, i, 'a'))
        for i in range(len(heights)):
            p_q.append((i, 0, 'p'))
            a_q.append((i, len(heights[0]) -1, 'a'))
        
        def bfs(q):
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            visited = set()
            while q:
                node = q.popleft()
                visited.add(node)
                # print(node)
                bool_list[node[0]][node[1]][node[2]] = True
                for d in directions:
                    r = node[0] + d[0]
                    c = node[1] + d[1]
                    if (r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0])
                        and (r,c) not in visited and heights[r][c] >= heights[node[0]][node[1]]):
                        visited.add((r,c))
                        q.append((r,c, node[2]))
        

        bfs(p_q)
        bfs(a_q)
        ans = []
        for i in range(len(bool_list)):
            for j in range(len(bool_list[0])):
                if bool_list[i][j]["a"] and bool_list[i][j]["p"]:
                    ans.append([i,j])
        
        return ans

        