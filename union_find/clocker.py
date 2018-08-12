import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.clock()
        func(*args, **kwargs)
        t2 = time.clock()
        print("运行耗时：" + str(t2 - t1))
    return wrapper




