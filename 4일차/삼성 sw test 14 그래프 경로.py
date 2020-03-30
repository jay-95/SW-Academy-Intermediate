T = int(input())
for test_case in range(1, T+1):
    V, E = map(int,input().split())
    Path_list = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E):
        a, b = map(int,input().split())
        Path_list[a-1][b-1] = 1

    S, G = map(int,input().split())
    visit = [False for _ in range(V)]
    visit[S-1] = True
    key = S
    stack = []
    
    while key != G:
        for i in range(V):
            if 1 in Path_list[key-1]:
                if Path_list[key-1][i] == 1 and visit[i] is False:
                    next_key = i+1
                    stack.append(key)
                    break
                elif Path_list[key-1][i] == 1 and visit[i] is True and stack:
                    next_key = ''
                    break
                
            elif 1 not in Path_list[key-1]:
                next_key = ''
                break
        if next_key != '':
            key = next_key
            visit[key-1] = True
            
        elif next_key == '' and stack:
            key = stack.pop()
        
        elif (next_key) == '' and not stack:
            break

    if key == G:
        result = 1
    else:
        result = 0

    print('#'+str(test_case), result)