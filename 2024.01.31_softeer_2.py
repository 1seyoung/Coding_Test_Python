import sys
from datetime import datetime

def main():

    sum_time = 0
    for i in range(5):
        in_time, out_time = input().split()
        in_time_ = datetime.strptime(in_time,"%H:%M")
        out_time_ = datetime.strptime(out_time,"%H:%M")

        gap = out_time_ - in_time_
        gap = gap.seconds /60

        sum_time += gap
    print(int(sum_time))

    




if __name__ == "__main__":
    main()