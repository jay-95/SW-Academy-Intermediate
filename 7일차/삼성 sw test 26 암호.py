T = int(input())
for test_case in range(1, T+1):
   N, M, K = map(int, input().split())
   S = list(map(int, input().split()))
   i = 0
   for j in range(K):
      i = (i + M) % len(S)
      if i == 0:
         S.insert(len(S),S[i-1]+S[i])
         i = len(S)-1
      else:
         S.insert(i,S[i-1]+S[i])
   
   print('#'+str(test_case), ' '.join(list(map(str, S[::-1][:10]))))