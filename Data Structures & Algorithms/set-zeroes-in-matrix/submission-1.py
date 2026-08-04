class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def helper(i,j):
            for r in range(len(matrix)):
                if matrix[r][j] == 0:
                    matrix[r][j] = None
                    helper(r,j)
                matrix[r][j] = None
            for c in range(len(matrix[0])):
                if matrix[i][c] == 0:
                    matrix[i][c] = None
                    helper(i,c)
                matrix[i][c] = None
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    helper(i,j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        

        
        