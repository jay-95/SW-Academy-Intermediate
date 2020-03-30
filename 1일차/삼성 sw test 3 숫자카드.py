T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input()))
    counter = [A.count(x) for x in range(1,10)]
    bmc = [y+1 for y,z in enumerate(counter) if z == max(counter)]
    maxcounter = max(bmc)
    print('#'+str(test_case),maxcounter,max(counter))
    