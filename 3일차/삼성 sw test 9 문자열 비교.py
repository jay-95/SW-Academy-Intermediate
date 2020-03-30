#.보이어 무어 알고리즘 이용

import time
start = time.time()

T = int(input())
for test_case in range(1, T+1):
    pattern = list(map(str,input()))
    text = list(map(str,input()))
    
    M = len(text)-1
    N = len(pattern)-1
    j = N
    k = j
    
    Result = 0
    
    while j <= M:   
        if text[j] != pattern[k]:
            l = k
            skip_num = 0
            while l >= 0:
                if text[j] != pattern[l]:
                    skip_num += 1
                    l -= 1
                else:
                    break
            j += skip_num
        elif text[j] == pattern[k]:
            if k == 0:
                Result = 1
                break
            else:
                j -= 1
                k -= 1

    print('#'+str(test_case),Result)
          
print("time :", time.time() - start)