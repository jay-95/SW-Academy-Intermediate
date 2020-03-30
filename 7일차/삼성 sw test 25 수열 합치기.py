T = int(input())
for test_case in range(1, T+1):
   N, M = map(int, input().split())
   S = list(map(int, input().split()))
   
   for i in range(M-1):
      U = list(map(int, input().split()))
      L = len(S)
      j = 0
      
      while j != L:
         if S[j] <= U[0]:
            j += 1
         
         else:
            break       
      idx = j
      
      S[idx:idx] = U
      
   print('#'+str(test_case), ' '.join(list(map(str, S[::-1][:10]))))