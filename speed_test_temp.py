from datetime import datetime
import time
import speedtest

def timer():
    times = ['00', '15', '30', '45']
    while(True):
        current_time = datetime.now().strftime('%H:%M')
        for quarter in times:
            if (current_time[3:5] == quarter):
                print("It is time")
            else:
                print("It is not time yet...")
                break
        time.sleep(60)



if __name__ == "__main__":
    timer()