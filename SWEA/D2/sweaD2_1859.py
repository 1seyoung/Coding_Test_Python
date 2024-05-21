"""
Greedy
N: 물건의 매매가 예측 가능한 기간(일)
하루에 최대 1 구매 가능
판매는 제한 x

최대 이익 : 싸게 사서 비싸게 팔기 (기본 논리)

1. 모든 경우의 수를 비교하는 방법
2. 어떤 최적화 알고리즘을 찾는 방법

2번이 시간복잡도 측면에서 좋을 듯 하다

 뒤에서부터 탐색이라는 힌트를 봄,,,ㅋ
"""
T = int(input())

for _ in range(T):
    N = int(input())
    info = list(map(int,list(input().split())))

    selling_point = -1 #인덱스

    max_benefit =0

    while 1 :
        i =0
        save = []
        current_benefit = info[selling_point]*len(save)

        if len(info) ==0:
            break

'''
for test_case in range(1, T + 1):
# ///////////////////////////////////////////////////////////////////////////////////
n=int(input())
price=list(map(int,input().split()))

result=0
max_num=0
for i in range(len(price)-1,-1,-1):

if price[i]>max_num:
max_num=price[i]
else:
result+=max_num-price[i]


print('#%d %d'%(test_case,result))
'''