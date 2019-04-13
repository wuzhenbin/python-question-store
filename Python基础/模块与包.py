

# -----输入日期， 判断这一天是这一年的第几天？-----
import datetime

def dayofyear(year,month,day):
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    return (date1-date2).days+1

dayofyear(2019,3,5)


# -----打乱一个排好序的list对象alist？------
import random

alist = [1,2,3,4,5]
random.shuffle(alist)
print(alist)