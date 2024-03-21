import datetime
import time
import calendar


def get_current_epoc_time():
    #return calendar.timegm(time.gmtime())*1000
    return int(time.time())
    #datetime.datetime.fromtimestamp(1347517370).strftime('%c') # change epoc time(1347517370) to original date (Sat Apr  4 11:32:15 2020)