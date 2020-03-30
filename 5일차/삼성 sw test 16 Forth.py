T = int(input())
for test_case in range(1, T+1):
    Forth_Str = list(map(str,input().split()))
    Stack_Num = []
    for i in range(len(Forth_Str)):
        if Forth_Str[i] == '+':
            if len(Stack_Num)<=1:
                print('#'+str(test_case), 'error')
                break
            
            else:
                Back = Stack_Num.pop()
                Forward = Stack_Num.pop()
                Stack_Num.append(Forward + Back)
            
        elif Forth_Str[i] == '-':
            if len(Stack_Num)<=1:
                print('#'+str(test_case), 'error')
                break
            
            else:
                Back = Stack_Num.pop()
                Forward = Stack_Num.pop()
                Stack_Num.append(Forward - Back)
        
        elif Forth_Str[i] == '*':
            if len(Stack_Num)<=1:
                print('#'+str(test_case), 'error')
                break
            
            else:
                Back = Stack_Num.pop()
                Forward = Stack_Num.pop()
                Stack_Num.append(Forward * Back)
            
        elif Forth_Str[i] == '/':
            if len(Stack_Num)<=1:
                print('#'+str(test_case), 'error')
                break
            
            else:
                Back = Stack_Num.pop()
                Forward = Stack_Num.pop()
                Stack_Num.append(Forward / Back)
        
        elif Forth_Str[i] == '.':
            Result = int(Stack_Num.pop())
            if not Stack_Num:
                print('#'+str(test_case), Result)
                break
            else:
                print('#'+str(test_case), 'error')
                break
            
        else:
            Stack_Num.append(int(Forth_Str[i]))