class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] < target:
                l = row * n + col + 1
            elif matrix[row][col] > target:
                r =  row * n + col - 1
            else:
                return True
        
        return False 
