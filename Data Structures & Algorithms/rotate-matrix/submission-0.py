class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        hmap = {}
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                x = j
                y = n - 1 - i
                hmap[(x,y)] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = hmap[(i,j)]
        
        
        