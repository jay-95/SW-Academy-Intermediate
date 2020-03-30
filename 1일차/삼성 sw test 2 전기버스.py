T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split()) #K = max Go, N = 도착점, A[M-1] = 충전기 위치
    A = list(map(int, input().split()))
    NowLoc = 0 #현 위치
    count = 0 #카운터
    Locheck = 0 #이전 위치 확인
    impossible = 0
    over = 0
    switch = 1
    
    while switch:
        
        check = 0 #정류장 확인
       
        i = K
        while i>=0:
               
            NowLoc = NowLoc + i
                
            if NowLoc >= N:
                over = 1
                print('#'+str(test_case),count)
                break
                
            j = M-1
            for j in range (j, -1, -1): #충전소 판별
                if NowLoc == A[j]:
                    check = 1
                    if i==0: #그런데 제자리 걸음이면 실패
                        count = 0
                        impossible = 1
                        break
                            
                    else: #아니면 루프 빠져 나가
                        count += 1
                        Locheck = NowLoc
                        break
                    
             
            if check == 1: #판별 결과 충전소
                break
                    
            elif check ==0: #아니면 한걸음 줄여서 가고, 현재위치 원위치로
                i = i-1
                NowLoc = Locheck
                
            elif impossible == 1:
                break
                    

        if impossible == 1:
            print('#'+str(test_case),count)
            break
        elif over == 1:
            break
        