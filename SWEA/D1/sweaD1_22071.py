# 표준 입출력 사용해야함


T = int(input())
answer =[]
for _ in range(T):
    data = input()

    data_lst = list(map(int,data.split()))



    aver = sum(data_lst)/len(data_lst)
    answer.append(round(aver))

for i in range(T):
    print(f"#{i+1} {answer[i]}")
