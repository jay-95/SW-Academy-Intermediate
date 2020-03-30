def Erase_str(string):
    stack = []
    for i in range(len(string)):
        stack.append(string[i])
        if i >= 1 and stack[i] == stack[i-1]:
            string = string[0:i-1]+string[i+1:len(string)]
            return Erase_str(string)
    
    return len(string)

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    print('#'+str(test_case), Erase_str(str1))
    