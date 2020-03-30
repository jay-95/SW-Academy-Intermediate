def backtrack(current_x, current_y, dir_index):
    global result
    print(dir_index)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
                  
    next_x = dx[dir_index] + current_x
    next_y = dy[dir_index] + current_y
    
        #진행 불가시
    if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N or Maze[next_x][next_y] == 1:
        if dir_index == 3: #방향 바꿀 수 없을 때
            if not visit_list: #시작 위치 시 종료
                return
            
            else: #pop
                before_x, before_y, before_dir = visit_list.pop()
                
                while before_dir == 3:
                    before_x, before_y, before_dir = visit_list.pop()
                    
                backtrack(before_x, before_y, before_dir+1)
        else:
            backtrack(current_x, current_y, dir_index + 1) #방향 바꿈
            
    
        #진행 가능시 stack 시키고 나아감
    elif Maze[next_x][next_y] == 0:
        Maze[current_x][current_y] = 1
        visit_list.append([current_x, current_y, dir_index])
        backtrack(next_x, next_y, 0)
    
        #도착시
    elif Maze[next_x][next_y] == 3:
        result = 1
        return

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visit_list = []
    result = 0

    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                start_x = i
                start_y = j
                break
    
    backtrack(start_x, start_y, 0)
    
    print('#'+str(test_case), result)