'''
    Rotten Oranges
    Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
    Each cell can have three values:
        The value 0 representing an empty cell.
        The value 1 representing a fresh orange.
        The value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    If this is impossible, return -1 instead.
    https://www.interviewbit.com/problems/rotten-oranges/
'''

def solve(A):
    from collections import deque
    # 0 Emtpy cell
    # 1 Fresh
    # 2 Rotten0
    m = len(A)
    n = len(A[0])
    temp = deque()
    bfs = deque()
    ans = 0
    for i in range(m):
        for j in range(n):
            if A[i][j] == 2:
                bfs.append((i, j))
    while bfs:
        temp = deque()
        for x, y in bfs:
            for xx, yy in ((x+1, y),(x-1, y), (x, y-1), (x, y+1)):
                if 0 <= xx < m and 0 <= yy < n:
                    if A[xx][yy] == 1:
                        A[xx][yy] = 2
                        temp.append((xx, yy))
        bfs = temp
        ans += bool(bfs)
    ans = ans if all( val!= 1 for row in A for val in row) else -1
    return ans

A = [
  [2, 0, 2, 2, 2, 0, 2, 1, 1, 0],
  [0, 1, 2, 0, 2, 0, 0, 1, 0, 1],
  [0, 1, 1, 1, 2, 0, 1, 1, 2, 1],
  [2, 0, 2, 0, 1, 1, 2, 1, 0, 1],
  [1, 0, 1, 1, 0, 1, 2, 0, 2, 2],
  [0, 2, 1, 1, 2, 2, 0, 2, 1, 2],
  [2, 1, 0, 2, 0, 0, 0, 0, 1, 1],
  [2, 2, 0, 2, 2, 1, 1, 1, 2, 2]
]
print(solve(A))
