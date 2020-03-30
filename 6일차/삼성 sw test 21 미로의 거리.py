def BFS(start_x, start_y):
    global result
    distance_level = 0
    Queue = []
    Queue.append((start_x, start_y, 0))
    while Queue:
        current_x, current_y, distance_level = Queue.pop(0)
        if not visited[current_x][current_y]:
            visited[current_x][current_y] = True
        
        for dir_index in range(4):
            next_x = dx[dir_index] + current_x
            next_y = dy[dir_index] + current_y
          
            if 0 <= next_x  < N and 0 <= next_y < N and (Maze[next_x][next_y] == 0 or Maze[next_x][next_y] == 3)and visited[next_x][next_y] is False:
                Queue.append((next_x, next_y, distance_level+1))
                
                if Maze[next_x][next_y] == 3:
                    result = distance_level
                    return result
        


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, T + 1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                start_x = i
                start_y = j
                break
    BFS(start_x, start_y)
    print('#'+str(test_case), result)