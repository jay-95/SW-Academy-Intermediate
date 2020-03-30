def Rotate(Q, N, i=0):
    if i == N:
        return Q[0]
    else:
        Q.append(Q.pop(0))
        return Rotate(Q, N, i+1)

T = int(input())
for test_case in range(1, T+1):
    M, N = map(int, input().split())
    Q = list(map(int, input().split()))
    answer = Rotate(Q, N)
    print('#'+str(test_case), answer)
    