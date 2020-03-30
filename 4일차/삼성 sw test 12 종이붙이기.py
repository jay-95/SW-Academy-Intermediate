T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    N_real = int(N/10)
    mem = [1, 3]
    for i in range(2,N_real):
        mem.append(mem[i-1]+2*mem[i-2])
    print('#'+str(test_case),mem[N_real-1])