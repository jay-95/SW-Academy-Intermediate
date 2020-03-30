T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    mem = []
    for i in str1:
        if i == '{':
            mem.append('}')
        elif i == '(':
            mem.append(')')
    
        elif i == '}' or i == ')':
            if not mem:
                result = 0
                break
            elif i == '}' and i != mem[-1]:
                result = 0
                break
            elif i == ')' and i != mem[-1]:
                result = 0
                break
            else:
                mem.pop()
    
    else:
        if not mem:
            result = 1
    if mem:
        result = 0
        
    print('#'+str(test_case), result)