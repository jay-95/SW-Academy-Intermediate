def binary_search(low, high, key, counter=0):
   
    if low>high:
        return False
    else:
        middle = (low + high)//2
            
        if key == middle:
            print(counter)
            return counter
        elif key < middle:
            counter += 1            
            return binary_search (low, middle, key, counter)
        elif key > middle:
            counter += 1
            return binary_search (middle, high, key, counter)
        
T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    A_counter = binary_search(1, P, A)
    B_counter = binary_search(1, P, B)
    if A_counter > B_counter:
        print('#'+str(test_case),'B')
    elif A_counter < B_counter:
        print('#'+str(test_case),'A')
    elif A_counter == B_counter:
        print('#'+str(test_case),'0')
