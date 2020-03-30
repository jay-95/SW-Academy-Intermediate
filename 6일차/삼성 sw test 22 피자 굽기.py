T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Q = []
    for j in range(N):
        Q.append([C.pop(0), j+1])
    k = 1
    while len(Q) != 1:
        Q[0][0] //= 2
        if Q[0][0] == 0:
            if C:
                Q.pop(0)
                Q.append([C.pop(0), N+k])
                k += 1
            else:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
    
    answer = Q[0][1]
    print('#'+str(test_case), answer)
        
        