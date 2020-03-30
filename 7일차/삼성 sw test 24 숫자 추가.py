T = int(input())
for test_case in range(1, T+1):
   N, M, L = map(int, input().split())
   Sequence = list(map(int, input().split()))
   
   for i in range(M):
      Index, Num = map(int, input().split())
      Sequence.insert(Index, Num)
      
   print('#'+str(test_case), Sequence[L])