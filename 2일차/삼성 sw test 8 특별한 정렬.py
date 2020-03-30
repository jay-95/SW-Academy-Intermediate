T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    
    for i in range(N): # 정렬
        for j in range (i+1, N):
            if i%2 == 0:
                if A[i]<A[j]:
                    A[i], A[j] = A[j], A[i]
            else:
                if A[i]>A[j]:
                    A[i], A[j] = A[j], A[i]
    
    print('#'+str(test_case), end = ' ')   #프린트    
    for k in range (10):
        if k == 9:
            print(A[k])
        else:
            print(A[k], end = ' ')