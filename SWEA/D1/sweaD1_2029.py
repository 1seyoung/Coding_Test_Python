T = int(input())

answers=[]

for i in range(T):
    a,b = map(int, input().split())

    answers.append(f"#{i+1} {a//b} {a%b}")

for answer in answers:
    print(answer)