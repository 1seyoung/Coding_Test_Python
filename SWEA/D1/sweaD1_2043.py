p, k = map(int,input().split())


if p>k:
    print(p-k+1)
else:
    print(p+1000 -k)