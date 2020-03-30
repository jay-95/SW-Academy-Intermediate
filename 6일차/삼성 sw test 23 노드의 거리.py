def DFS_Node(key):
    while key != G:
        distance_level = 0
        Queue = []
        Queue.append((key, distance_level))
        while Queue:
            key, distance_level = Queue.pop(0)
            visit[key-1] = True
            if 1 in Path_list[key-1]:
                for i in range(V):
                    if Path_list[key-1][i] == 1 and visit[i] is False:
                        if i+1 == G:
                            return distance_level+1
                        else:
                            Queue.append((i+1, distance_level+1))
                        
        if not Queue and key != G:
            return 0


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int,input().split())
    Path_list = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E):
        a, b = map(int,input().split())
        Path_list[a-1][b-1] = 1
        Path_list[b-1][a-1] = 1

    S, G = map(int,input().split())
    visit = [False for _ in range(V)]
    visit[S-1] = True
    key = S
    
    print('#'+str(test_case), DFS_Node(key))