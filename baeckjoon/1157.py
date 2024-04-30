

input = input().upper()

if input.isalpha() == False:
    exit()

dict = { }

for i in input:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

max = max(dict.values())
max_key = []

for key, value in dict.items():
    if value == max:
        max_key.append(key)

if  len(max_key) >1:
    print("?")
else:
    print(max_key[0])