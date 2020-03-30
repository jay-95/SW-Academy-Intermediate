T = int(input())
for test_case in range(1, T+1):
   N, M, L = map(int, input().split())
   S = list(map(int, input().split()))
   for i in range(M):
      Command = list(map(str, input().split()))
      if Command[0] == "I":
         S.insert(int(Command[1]), int(Command[2]))
      elif Command[0] == "D":
         S.pop(int(Command[1]))
      elif Command[0] == "C":
         S[int(Command[1])] = int(Command[2])
         
   if L > len(S)-1:
      answer = -1
   else:
      answer = S[L]
   print('#'+str(test_case), answer)
         