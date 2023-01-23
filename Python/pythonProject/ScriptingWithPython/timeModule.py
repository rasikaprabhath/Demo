import time

def find_Time():

    epc=time.time()
    real_time=time.localtime(epc)
    print(epc)
    print(real_time.tm_year)
    print(time.ctime(epc))
find_Time()
