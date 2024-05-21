a, b = map(int, input().split())
#가위 1 바위 2 보 3
if a ==1 :
    if b == 2:
        print("B")
    else:
        print("A")
elif a==2:
    if b == 1:
        print("A")
    else:
        print("B")
elif a==3:
    if b==1:
        print("B")
    else:
        print("A")