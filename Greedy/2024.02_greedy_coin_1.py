import time
start_time = time.time()

def conin_change(money):

    coin_lst = [500,100,50,10]
    count =0

    for coin in coin_lst:
        count += money//coin
        money %= coin

    print(count)

    



if __name__== "__main__":
    start_time = time.time()


    money = int(input("input money :"))
    conin_change(money)

    end_time = time.time()
    print(f"{start_time}-{end_time}")