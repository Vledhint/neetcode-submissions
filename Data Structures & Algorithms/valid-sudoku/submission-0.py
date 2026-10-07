class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                # Cada visita es una columna
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                
                # print(f"Agregando valor: {board[i][j]}")
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
                # print(f"Valor de square: {(i // 3, j // 3)}")


        return True
