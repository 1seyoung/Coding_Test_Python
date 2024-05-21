from collections import defaultdict
T = int(input())

answers =[]

for _ in range(T):
    t = int(input())

    score = list(map(int, input().split()))
    score.sort(reverse=True)

    max_count = defaultdict(int)

    for num in score:
        max_count[num] += 1

    tmp = max(max_count,key= max_count.get)

    answers.append(tmp)

for i,answer in enumerate(answers):
    print(f"#{i+1} {answer}")

