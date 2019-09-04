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
    # for k in range(4):
    #     next_x = src[0]
    #     next_y = src[1]
    #     # next_x = next_x + directions_x[k]
    #     # next_y = next_y + directions_y[k]
    #     if(0 <= next_x < m and
    #       0 <= next_y < n):
    #         d.append({'coord':[next_x, next_y], 
    #               'dirc':[directions_x[k], directions_y[k]]})
    #         # dist[next_x][next_y] += 1
    # print(d)
    # print(dist)
    while d:
        # print("_____________")
        # for _ in d:
        #     print(_)
        # for _ in dist:
        #     print(_)
        # print("_____________")
        item = d.popleft()
        coord = item['coord']
        dirc = item['dirc']
        next_x = coord[0]
        next_y = coord[1]
        # print(item)

        if not (next_x, next_y) in visited:
            if (0 <= next_x < m and
                0 <= next_y < n and
                not A[next_x][next_y]):
                    # print("hello")
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
                        # print("ijhihiihiu")
                        flag = True
                    if flag:
                        visited.add((next_x, next_y))
                        dist[next_x][next_y] = dist[next_x - dirc[0]][next_y - dirc[1]] + 1
                        if [next_x, next_y] == dest:
                            # print("ho gaya", dist)
                            return dist[next_x][next_y]
                        # print("halo")
                        for k in range(4):
                            next_x = t1
                            next_y = t2
                            next_x = next_x + directions_x[k]
                            next_y = next_y + directions_y[k]
                            # print(next_x, next_y, "check")
                            if(0 <= next_x < m and
                                0 <= next_y < n and
                                A[next_x][next_y] == 0):
                                d.append({'coord':[next_x, next_y], 
                                        'dirc':[directions_x[k], directions_y[k]]})   
                                # dist[next_x][next_y] = dist[coord[0]][coord[1]]
                    elif A[next_x + dirc[0]][next_y + dirc[1]] == 0:
                        d.append({'coord':[next_x + dirc[0], next_y + dirc[1]], 
                                    'dirc':[dirc[0], dirc[1]]})
                        dist[next_x][next_y] = dist[next_x - dirc[0]][next_y - dirc[1]] + 1
                    # print(d, dist)
                    # d.append({'coord':[next_x + 0, next_y - 1], 'dirc':[0, -1]})
                    # d.append({'coord':[next_x + 0, next_y + 1], 'dirc':[0, +1]})
                    # d.append({'coord':[next_x - 1, next_y + 0], 'dirc':[-1, 0]})
                    # d.append({'coord':[next_x + 1, next_y + 0], 'dirc':[+1, 0]})
    # print(dist)
    return -1

A = [   [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
B = [0, 4]
C = [4, 4]
print("182")
print(solve(A, B, C) - 1)