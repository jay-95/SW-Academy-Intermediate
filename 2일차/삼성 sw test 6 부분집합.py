arr = [x for x in range(1, 13)]
n = len(arr)
subset_list = []
T = int(input())
for i in range(1<<n): #부분함수 리스트 구하기
    sub_set = []
    for j in range(n):
        if i & (1<<j):
            sub_set.append(arr[j])
    subset_list.append(sub_set)
for test_case in range (1, T+1):
    counter = 0
    N, K = map(int, input().split())
    for k in range (len(subset_list)):
        if len(subset_list[k]) == N and sum(subset_list[k]) == K:
            counter += 1
            
    print('#'+str(test_case), counter)