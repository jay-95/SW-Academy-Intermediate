def backtrack(i):
    global Min_Sum
    
    for j in range(N):
        
        #약속된 노드일 때 경로 추가
        if promising(i, j):
            visit.append([i, j])
            #최대 깊이 도달 시        
            if i == N-1:  
                #합 계산 및 최소 합 계산
                Sum = 0
                for b in visit:
                    Sum = Sum + Array[b[0]][b[1]]
                if Min_Sum == 0:
                    Min_Sum = Sum
                else:
                    if Sum < Min_Sum:
                        Min_Sum = Sum
                        
                visit.pop()
                
            #최대 깊이 아닐 때    
            else:
                #합 계산시 이미 최소 합보다 크면 더 이상 진행 필요 없음
                Sum = 0
                for b in visit:
                    Sum = Sum + Array[b[0]][b[1]]
                if Sum > Min_Sum:
                    if Min_Sum != 0:
                        visit.pop()
                        continue
                #아닐 시 진행    
                backtrack(i+1)
    
        
    if not visit:
        return
    
    else:
        visit.pop()
       

#약속 노드 정의
def promising(i, j):
    Result = True
    for a in visit:
        if a[1] == j:
            Result = False
    return Result

    

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    Array = [list(map(int, input().split())) for _ in range(N)]
    Min_Sum = 0
    visit = []
    backtrack(0)
    
    print('#'+str(test_case), Min_Sum)