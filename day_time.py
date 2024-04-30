import datetime
import pytz

timezone_obj = pytz.timezone('Asia/Kolkata')
current_weekday = datetime.datetime.now(timezone_obj).weekday()
current_hour = datetime.datetime.now(timezone_obj).hour

wday_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

if __name__ == "__main__":
    print(wday_dict[current_weekday])
    print(f'Current time: {current_hour}')
    