class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                for k in range(j + 1, 9):
                    if board[i][j] == board[i][k]:
                        return False

        for j in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue
                for k in range(i + 1, 9):
                    if board[i][j] == board[k][j]:
                        return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] == ".":
                            continue
                        for k in range(i, box_row + 3):
                            for l in range(box_col, box_col + 3):
                                if i == k and j == l:
                                    continue
                                if board[i][j] == board[k][l]:
                                    return False

        return True
        