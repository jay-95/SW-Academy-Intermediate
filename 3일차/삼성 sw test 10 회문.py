T = int(input())
for test_case in range(1, T+1):
    N,M = map(int, input().split())
    text = [list(map(str,input())) for _ in range(N)]
    result = None
    #가로
    for i in range(N):
        for j in range(N-M+1):
            A = text[i][j:j+M]
            A1 = A[0:M//2]
            A2 = A[M-(M//2):M]
            A2 = A2[::-1]
            if A1 == A2:
                result = A
                break
        if result is not None:
            break

    if result is None:
        text1 = list(map(list,zip(*text)))
        #세로
        for k in range(N):
            for l in range(N-M+1):
                B = text1[k][l:l+M]
                B1 = B[0:M//2]
                B2 = B[M-(M//2):M]
                B2 = B2[::-1]
                if B1 == B2:
                    result = B
                    break
            if result is not None:
                break
                
    print('#'+str(test_case),''.join(result))