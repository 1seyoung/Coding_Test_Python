T = int(input())
answer=[]
for i in range(T):
    string = input()

    if string[::-1] == string:
        print(string[::-1])
        answer.append(1)
    else:
        answer.append(0)
        print(string[::-1])

for i in range(T):
    print(f"#{i+1} {answer[i]}")