from datetime import datetime
import time
import speedtest
import csv


STAUTS_OUTPUT_FILE = 'output/status.txt'
DATA_FILE = 'output/output_file.csv'


'''Outputs current status to txt file'''
def write_status(output_file, output):
    with open(output_file, 'a') as writer:
                    writer.write(output)


'''Run the test_speed() function at every quarter of the hour precisely.'''
def timed_sample_output():
    SECS_BETWEEN_LOOPS = 120 # How long between each "not time yet" message
    times = ['00', '15', '25', '45'] # List of quarter-hours

    
    # counter = 1 # keeps track of how many loop loops have been looped
    while(True): # Loop to continually test current time against quarter-hours
        current_time = datetime.now().strftime('%H:%M')
        is_time_message = "It is time {}\n".format(current_time)
        # not_time_message = "It is not time yet... {}\n".format(current_time)
        for quarter in times:
            if (current_time[3:5] == quarter):
                write_status(STAUTS_OUTPUT_FILE, is_time_message)
                test_speed(current_time)
                time.sleep(60) # Ensures a test isn't called twice for the same quarter-hour
                break
        #     elif (quarter == times[3]):
        #         if (counter >= SECS_BETWEEN_LOOPS): # for every however many seconds, a "not time yet" message displays
        #             # write_status(STAUTS_OUTPUT_FILE, not_time_message)
        #             counter = 0
        # counter += 1
        time.sleep(1)


'''Takes a sample of internet connection Down/Up speeds and puts the results in a dictionary
    Outputs the results of each test onto console'''
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
    write_status(STAUTS_OUTPUT_FILE, "Trial for time: {} completed\n{}\n".format(curr_time, output))
    write_to_file(output)


'''Takes a test conducted by test_speed() and sticks it in a csv file.'''
def write_to_file(output):
    with open(DATA_FILE, 'a') as write_file:
        columns = ['Date', 'Time', 'Download', 'Upload']
        writer = csv.DictWriter(write_file, fieldnames=columns)
        # writer.writeheader() -- Include this if you want a header with the data
        writer.writerow(output)


'''Run the program!'''
if __name__ == "__main__":
    timed_sample_output()
