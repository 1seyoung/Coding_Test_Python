from datetime import datetime

T = int(input())

answers=[]
for i in range(T):
    data = input()

    try:
        datetime.strptime(data,'%Y%m%d')
        answers.append(f"#{i+1} {data[0:4]}/{data[4:6]}/{data[6:8]}")
    except(ValueError):
        answers.append(f"#{i+1} {-1}")

for answer in answers:
    print(answer)