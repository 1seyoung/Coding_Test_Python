T= int(input())


for _ in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = [[0 for j in range(N+1)]for i in range(N+1)]

    max_flies = 0

    # 누적합 배열 초기화 (N+1) * (N+1)
    prefix_sum = [[0 for j in range(N)] for i in range(N+1)]

    #누적합 구하ㅣㄱ

    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix_sum[i,j] = arr[i-1][j-1] +
            #i,j의 누적합은 구하려는 배열 arr 의 [i-1][j-1] 위치의 값과


            '''
arr:                prefix_sum:
1  2  3  4  5       0  0  0  0  0  0
6  7  8  9  10      0  1  3  6  10 15
11 12 13 14 15      0  7 16 27 40 55
16 17 18 19 20      0 18 39 63 90 120
21 22 23 24 25      0 34 72 114 160 210
                   0 55 115 180 250 325
  
    '''