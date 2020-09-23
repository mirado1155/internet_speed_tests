from datetime import datetime
import time
import speedtest
import csv


# This function will run the test_speed() function at every quarter of the hour precisely.
def timed_sample_output():

    SECS_BETWEEN_LOOPS = 120 # How long between each "not time yet" message
    times = ['00', '15', '30', '45'] # List of quarter-hours

    # Loops to continually test current time against quarter-hours
    while(True):
        counter = 1 # keeps track of how many loop loops have been looped
        current_time = datetime.now().strftime('%H:%M')
        for quarter in times:
            if (current_time[3:5] == quarter):
                print("It is time {}".format(current_time))
                test_speed(current_time)
                # This ensures a test isn't called twice for the same quarter-hour
                time.sleep(60)
                break
            elif (quarter == times[3]):
                if (counter == SECS_BETWEEN_LOOPS): # basically for every however many seconds, a "not time yet" message displays
                    print("It is not time yet... {}".format(current_time))
        time.sleep(1)


# Takes a sample of internet connection Down/Up speeds and puts the results in a dictionary
# Outputs the results of each test onto console
def test_speed(curr_time):
    
    SPEED_DIVISOR = 1000000 # for converting bits per second into Mbps

    s = speedtest.Speedtest()
    download_time = s.download()
    upload_time = s.upload()
    today = datetime.now().date()
    output = {
        "Date":today,
        "Time": curr_time,
        "Download":round((download_time / SPEED_DIVISOR), 2),
        "Upload":round((upload_time / SPEED_DIVISOR), 2)
    }
    print("Trial for time: {} completed".format(curr_time))
    print(output)
    write_to_file(output)


# Takes a test conducted by test_speed() and sticks it in a csv file.
def write_to_file(output):
    with open('output_file.csv', 'a') as write_file:
        columns = ['Date', 'Time', 'Download', 'Upload']
        writer = csv.DictWriter(write_file, fieldnames=columns)
        # writer.writeheader() -- Include this if you want a header with the data
        writer.writerow(output)


# Run the program!
if __name__ == "__main__":
    timed_sample_output()
