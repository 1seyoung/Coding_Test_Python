
T = int(input())

answer = []
for _ in range(T):

    test_case = list(map(int, input().split()))
    answer.append(max(test_case))
    '''max_value = max(test_case)'''

for i in range(T):
    print(f"#{ i +1} {answer[i]}")
