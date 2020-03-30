def R_S_P(left, right):
    if (Card_List[left-1] == Card_List[right-1]):
        return left
    elif (Card_List[left-1] == 2 and Card_List[right-1] == 1) or (Card_List[left-1] == 1 and Card_List[right-1] == 3) or (Card_List[left-1] == 3 and Card_List[right-1] == 2):
        return left
    return right

def Winner(start, end):
    if start == end:
        return start
    
    middle = (start+end)//2
    first_value = Winner(start, middle)
    second_value = Winner(middle+1, end)
    return R_S_P(first_value, second_value)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    Card_List = list(map(int, input().split()))
    start = 1
    end = N
    print('#'+str(test_case), Winner(start, end))