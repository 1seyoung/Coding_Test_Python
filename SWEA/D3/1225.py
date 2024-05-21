answers=[]

for j in range(10):
    n = int(input())

    numbers = list(map(int,input().split()))


    i =1

    while(1):

        a = numbers[0] -i
        if a <=0:
            a=0
            del numbers[0]
            numbers.append(a)
            break
        else:
            del numbers[0]
            numbers.append(a)


        i = i+1
        if i ==6:
            i = 1
    answers.append(numbers)

for j, number in enumerate(answers):
    print(f"#{j+1} {' '.join(map(str, number))}")
