def solveNQueens(n):
    ans = []
    chess = ['.'*n for i in range(n)]
    def check(row, col, n, board):
        duprow = row
        dupcol = col
        while row>=0 and col>=0:
            if board[row][col] == 'Q':
                return False
            col-=1
            row-=1
        row = duprow
        col = dupcol
        while col>=0:
            if board[row][col] == 'Q':
                return False
            col-=1
        row = duprow
        col =dupcol
        while row<n and col>=0:
            if board[row][col] == 'Q':
                return False
            row +=1
            col -=1
        return True

    def solve(col, n, chess):
        if col == n:
            ans.append(chess[:])
            return
        for i in range(n):
            if check(i, col, n, chess):
                chess[i] = chess[i][:col] + 'Q' + chess[i][col+1:]
                solve(col+1, n, chess)
                chess[i] = chess[i][:col] + '.' + chess[i][col+1:]
    solve(0, n, chess)
    return ans
print(solveNQueens(3))