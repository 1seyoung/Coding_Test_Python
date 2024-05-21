
N = int(input())

test_case = list(map(int,input().split()))


test_case.sort()

mid = round(N/2)


print(test_case[mid-1])