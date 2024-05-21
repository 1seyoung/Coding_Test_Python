T = int(input())
answers =[]
for _ in range(T):
    N = int(input())

    arr = [[0 for j in range(N)] for i in range(N)]
    for n in range(N):
        arr[n][0] = 1

    for x in range(1,N):
        for y in range(1,N):
            arr[x][y] = arr[x-1][y-1] + arr[x-1][y]

    answers.append(arr)

for i,answer in enumerate(answers):
    print(f"#{i+1}")

    for row in answer:
        for i in range(len(answer)):
            if row[i] != 0:
                print(row[i],end=' ')
        print()
