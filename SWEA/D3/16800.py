T =int(input())
answers =[]
for _ in range(T):
    N = int(input())

    #최대 공약수 찾기
    divor = []
    for i in range(1,int(N**0.5)+1):
        if N%i ==0: #i로 나눠 떨어지면
            divor.append(i)
            if i !=N // i: # 중복 제거 > i dhk N//i가 다를때만 N//i 추가
                divor.append(N//i)

    min_move = float('inf')

    for i in divor:
        j =N//i

        min_move = min(min_move,i+j-2)

    answers.append(min_move)

for i in range(T):
    print(f"#{i+1} {answers[i]}")