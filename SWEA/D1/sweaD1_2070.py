
T = int(input())

answer =[]

for _ in range(T):
    a, b = map(int, input().split())

    if a > b:
        answer.append(">")
    elif a == b :
        answer.append("=")
    else:
        answer.append("<")

for i in range(T):
    print(f"#{i+1} {answer[i]}")