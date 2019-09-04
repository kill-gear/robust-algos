'''
    Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.
    1 represents a wall in a matrix and 0 represents an empty location in a wall.

    There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won’t stop rolling until hitting a wall.
    When the ball stops, it could choose the next direction.

    Given two array of integers of size B and C of size 2
    denoting the starting and destination position of the ball.

    Find the shortest distance for the ball to stop at the destination.
    The distance is defined by the number of empty spaces traveled by the ball
    from the starting position (excluded) to the destination (included).
    If the ball cannot stop at the destination, return -1.
    https://www.interviewbit.com/problems/shortest-distance-in-a-maze/
'''

def solve(A, B, C):
    from collections import deque
    src = B
    dest = C
    m = len(A)
    n = len(A[0])
    dist = [ [0 for i in range(n)] for i in range(m)]
    d = deque()
    visited = set()
    # 1 2 
    # 3 4
    next_x = src[0]
    next_y = src[1]
    directions_x = [0, 0, -1, +1]
    directions_y = [-1, +1, 0, 0]
    d.append({'coord':[next_x, next_y], 'dirc':[0, 0]})
    while d:
        item = d.popleft()
        coord = item['coord']
        dirc = item['dirc']
        next_x = coord[0]
        next_y = coord[1]

        if not (next_x, next_y) in visited:
            if (0 <= next_x < m and
                0 <= next_y < n and
                not A[next_x][next_y]):
                    t1 = next_x
                    t2 = next_y
                    flag = False            
                    if (0 <= next_x + dirc[0] < m and
                        0 <= next_y + dirc[1] < n and
                        A[next_x + dirc[0]][next_y + dirc[1]] == 1 
                        or dirc == [0,0]):
                        flag = True
                    elif (next_x + dirc[0] < 0 or next_x + dirc[0] >= m or
                          next_y + dirc[1] < 0 or next_y + dirc[1] >= n):
                        flag = True
                    if flag:
                        visited.add((next_x, next_y))
                        dist[next_x][next_y] = dist[next_x - dirc[0]][next_y - dirc[1]] + 1
                        if [next_x, next_y] == dest:
                            return dist[next_x][next_y]
                        for k in range(4):
                            next_x = t1
                            next_y = t2
                            next_x = next_x + directions_x[k]
                            next_y = next_y + directions_y[k]
                            if(0 <= next_x < m and
                                0 <= next_y < n and
                                A[next_x][next_y] == 0):
                                d.append({'coord':[next_x, next_y], 
                                        'dirc':[directions_x[k], directions_y[k]]})   
                    elif A[next_x + dirc[0]][next_y + dirc[1]] == 0:
                        d.append({'coord':[next_x + dirc[0], next_y + dirc[1]], 
                                    'dirc':[dirc[0], dirc[1]]})
                        dist[next_x][next_y] = dist[next_x - dirc[0]][next_y - dirc[1]] + 1
    return -1

A = [   [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
B = [0, 4]
C = [4, 4]
print(solve(A, B, C) - 1)