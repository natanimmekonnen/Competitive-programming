# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        set_col= set()
        set_anti=set()
        set_dia=set()

        def plausible(row,col):
            return not (col in set_col or (row-col) in set_anti or (row+col) in set_dia)
        board=[["." for i in range(n)] for j in range(n)]
        result=[]
        def backtr(row):
            if row==n:
                copy=[]
                for i in range(n):
                    string="".join(board[i])
                    copy.append(string)
                result.append(copy)
                return
            for col in range(n):
                if plausible(row,col):
                    set_col.add(col)
                    set_anti.add(row-col)
                    set_dia.add(row+col)
                    board[row][col]="Q"
                    backtr(row+1)
                    set_col.remove(col)
                    set_anti.remove(row-col)
                    set_dia.remove(row+col)
                    board[row][col]="."
        backtr(0)
        return result
                    


        