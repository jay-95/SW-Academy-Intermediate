def backtrack(i):
    global Min_Sum
    global Sum
    
    if Sum > Min_Sum:
        if Min_Sum != 0:
            return
    
    if i == N:
        if Min_Sum == 0:
            Min_Sum = Sum
        else:
            if Sum < Min_Sum:
                Min_Sum = Sum
        return
    for j in range(N):
        if not visit[j]:
            visit[j] = True
            Sum += Array[i][j]
            backtrack(i+1)
            Sum -= Array[i][j]
            visit[j] = False
    
    
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    Array = [list(map(int, input().split())) for _ in range(N)]
    visit = [False]*N
    Sum = 0
    Min_Sum = 0
    backtrack(0)
    
    print('#'+str(test_case), Min_Sum)