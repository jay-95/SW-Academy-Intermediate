T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    letter_dict = {}
    for i in str1:
        if i not in letter_dict:
            letter_dict[i] = 0
    
    for j in letter_dict:
        for k in range(len(str2)):
            if j == str2[k]:
                letter_dict[j] += 1
                
    Result = max(letter_dict.values())
    print('#'+str(test_case),Result)       