def Near_List_Sum(List,NearNumber): #이웃값 합 경우의 수 리스트 만들기
    Result_List = [sum(List[i:i+NearNumber]) for i in range (0, len(List)-NearNumber+1)]
    return Result_List

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    Sum_List = Near_List_Sum(A,M)
    Result = max(Sum_List)-min(Sum_List)
    print('#'+str(test_case),Result)
    