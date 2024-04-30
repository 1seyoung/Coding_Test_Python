'''
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.


첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

1. n = input()  >> n 입력받기
2. array = [] >> 숫자 담을 빈 리스트 정의
3. for _ in range(n)
    
    a = input()
    
    array.append(a)
    
4. 산술평균 계산 > 출력
    1. array list 요소 합 / n( = len(array))
5. 중앙값 계산 > 출력
    1. 증가하는 순서로 나열 > sort   **array.sort()**
    2. 중앙값 **array[len(array)//2]**
6. 최빈값 계산 > 출력
    1. collection 라이브러리를 사용해도됨
        1. from collection import Counter >> 나중에 사용해보기
    2. //직접구현해도됨
7. 범위 계산 > 출력

'''
import sys

n = int(input())

array = []

for _ in range(n):
    #a = int(input())
    a = int(sys.stdin.readline())
    array.append(a)

# 산술평균
aver = sum(array)/n
print(round(aver))

#중앙값
array.sort()
mid = array[len(array)//2]
print(mid)

#최빈값
array_count ={}

for i in array:
    if i not in array_count:
        array_count[i]=1
    else:
        array_count[i]+=1

max = max(array_count.values())
max_key =[]

for key, value in array_count.items():
    if value == max:
        max_key.append(key)

max_key.sort()
if len(max_key) >1:
    print(max_key[1])
else:
    print(max_key[0])

#범위
range = array[n-1] - array[0]
print(range)
