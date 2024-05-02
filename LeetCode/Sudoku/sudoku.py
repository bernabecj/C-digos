board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


class Solution:
    def check_empty_cell(self, board):
        for index1, row in enumerate(board):
            for index2, ele in enumerate(row):
                if ele == ".":
                    return (index1, index2)
        return False

    def is_valid(self, board, row, col, num):
        if str(num) in board[row]:
            return False

        for i in range(9):
            if board[i][col] == str(num):
                return False

        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == str(num):
                    return False

        return True

    def solve_sudoku(self, board):
        empty_cell = self.check_empty_cell(board)

        if empty_cell == False:
            return True

        row, col = empty_cell
        for ele in range(1, 10):
            if self.is_valid(board, row, col, ele):
                board[row][col] = str(ele)
                if self.solve_sudoku(board):
                    return True

                board[row][col] = "."

    def print_board(self, board):
        for row in board:
            print(row)


if __name__ == "__main__":
    obj = Solution()
    if obj.solve_sudoku(board):
        obj.print_board(board)
    else:
        print("There is no solution")
