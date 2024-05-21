'''

문자열 > 정규표현식 사용?
'''



N = int(input())
check_list =["3","6","9"]
numbers = [str(i+1) for i in range(N)]

for number in numbers:
    a = list(number)
    if all(item not in a for item in check_list):
        print(int(number), end=" ")
    else:
        count = sum(a.count(item) for item in check_list)
        print("-"*count, end=" ")