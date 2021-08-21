class Solution(object):
        
    def isSquare(self, matrix, x, y, length):
        if length == 1:
            if matrix[x][y] == 1:
                return True
            else:
                return False
        for i in range(length):
            if matrix[x+i][y+length-1] != 1:
                return False
        for i in range(length):
            if matrix[x+length-1][y+i] != 1:
                return False
        return True
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = 1
                while True:
                    if not (i+length<=m and j+length<=n) or not self.isSquare(matrix, i, j, length):
                        length -= 1
                        break
                    else:
                        length += 1
                count += length
                print(i, j)
                print(length)
        return count
