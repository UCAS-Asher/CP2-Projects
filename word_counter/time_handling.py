#Asher Wangia, Word Counter
import datetime
import pytz


def time_set():
    current_time = datetime.datetime.now(pytz.timezone('US/Mountain'))

    year = str(current_time.year)

    month = str(current_time.month)

    day = str(current_time.day)

    hour = str(current_time.hour)

    minute = str(current_time.minute)
   
    if int(minute) < 10:
        minute = "0"+ minute
    else:
        pass

    zone = pytz.all_timezones

    time = (hour + ":" + minute + ", " + month + "/" + day + "/" + year)
    
    return "Time: " + time