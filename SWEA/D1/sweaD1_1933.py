N = int(input())

answers=[]

for i in range(1,N+1):
    if N%i ==0:
        answers.append(i)
    else:
        pass

for answer in answers:
    print(answer,end=" ")