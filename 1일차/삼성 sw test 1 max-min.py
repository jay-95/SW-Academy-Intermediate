T = int(input())

for test_case in range(1, T + 1):
      
    N = int(input())
    a = map(int, input().split())
    A = list(a)
    R = max(A) - min(A)
    
    
    print('#',test_case, R)