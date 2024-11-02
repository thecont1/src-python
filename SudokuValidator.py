from typing import List
import time

class SudokuValidator:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidLine(row):
                # print("Gotchee in row", row)
                return False
            
        for column in list(zip(*board)):
            if not self.isValidLine(column):
                # print("Gotchee in column", column)
                return False
            
        for i in range(1, 10, 3):
            matrix = []
            for j in range(1, 10, 3):
                matrix = board[i-1][j-1:j+2] + board[i][j-1:j+2] + board[i+1][j-1:j+2]
                if not self.isValidLine(matrix):
                    # print("Gotchee in matrix", matrix)
                    return False

        return True

    def isValidLine(self, line: List[str]) -> bool:
        checkSum = list(range(10))
        for n in range(1, 10):
            if line[n-1] != '.':
                if checkSum[int(line[n-1])] > 0:
                    checkSum[int(line[n-1])] = 0
                else:
                    return False
        return True

class SuperFastSudokuValidator:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in square[r//3,c//3]:
                    return False
                
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                square[r//3,c//3].add(board[r][c])
        return True

        
List1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".","1","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
List2 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
L = List1

start_time = time.time()
result = SudokuValidator().isValidSudoku(L)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"SudokuValidator returns {str(result).upper()} in {elapsed_time*1000000} microseconds")

start_time = time.time()
result = SuperFastSudokuValidator().isValidSudoku(L)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"SuperFastSudokuValidator returns {str(result).upper()} in {elapsed_time*1000000} microseconds")
