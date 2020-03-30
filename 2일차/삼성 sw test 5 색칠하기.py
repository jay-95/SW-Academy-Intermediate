T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    System = [[0 for _ in range(10)] for _ in range(10)] #좌표생성
    for search_case in range(N): #색칠 횟수 N번 입력
        paint = list(map(int, input().split()))
        for i in range (paint[0], paint[2]+1):
            for j in range (paint[1], paint[3]+1): #색칠하기
                if System[i][j] != paint[4]: #같은 색깔일때 색칠 안함
                    System[i][j] += paint[4]
    
    counter = 0
    for k in range (len(System)):
        counter += System[k].count(3)
    result = counter
    print('#'+str(test_case),result)