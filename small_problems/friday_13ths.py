from datetime import datetime

def friday_the_13ths(year, date=13):
    thirteenths = []
   
    for month in range(1, 13):
        thirteenths.append(datetime(year, month, date).weekday())

    print(thirteenths.count(4))

friday_the_13ths(1986)      # 1
friday_the_13ths(2015)      # 3
friday_the_13ths(2017)      # 2