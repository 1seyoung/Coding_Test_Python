
T = int(input())
sum_lst = []
for i in range(T):
    data = input()
    lst = list(map(int, data.split()))

    sum = 0

    for num in lst:
        if num % 2 != 0:
            sum += num
        else:
            pass
    sum_lst.append(sum)

for i in range(T):
    print(f"#{i+1} {sum_lst[i]}")

