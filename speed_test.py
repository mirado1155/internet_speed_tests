from datetime import datetime
import time
import speedtest
import csv
import json
import matplotlib.pyplot as pyplot

# def timer():
#     stop_time = input("Please enter a stopping time: ")
    # while(True):
    #     frmt = '%M'
    #     current_time = datetime.now().strftime('%I:%M')
    #     tdelta = datetime.strptime(stop_time, frmt) - datetime.strptime(current_time, frmt)
    #     print(tdelta)
    #     if(stop_time != current_time):
    #         print("it is not time")
    #         # time.sleep(10)
    #     else:
    #         print("it is time")
    #         break


    # frmt = '%I:%M'
    # current_time = datetime.now().strftime('%I:%M')
    # tdelta = datetime.strptime(stop_time, frmt) - datetime.strptime(current_time, frmt)
    # time_diff = int((tdelta.total_seconds()) / 60)
    # print(time_diff)
    # print(tdelta)
    # interval = 15
    # next_time = current_time + interval
    # print(next_time)


    # time_one = '10:33:26'
    # time_two = '11:15:49' # for example
    # frmt = '%H:%M'
    # tdelta = datetime.strptime(time_two, frmt) - datetime.strptime(time_one, frmt)
    # print(tdelta)


def test_speed(rest_period):
    SPEED_DIVISOR = 1000000
    s = speedtest.Speedtest()
    # results = []
    count = 1
    while(True):
        curr_time = datetime.now()
        download_time = s.download()
        upload_time = s.upload()
        today = datetime.now().date()
        output = {
            "Date":today,
            "Trial Number":(count),
            "Time": curr_time.strftime('%I:%M'),
            "Download":round((download_time / SPEED_DIVISOR), 2),
            "Upload":round((upload_time / SPEED_DIVISOR), 2)
        }
        # results.append(output)
        print("Trial number {} completed".format(count))
        write_to_file(output)
        print(output)
        count += 1
        time.sleep(rest_period * 60)
    # plot_results(results)


def write_to_file(output):
    with open('output_file.csv', 'a') as write_file:
        columns = ['Date', 'Trial Number', 'Time', 'Download', 'Upload']
        writer = csv.DictWriter(write_file, fieldnames=columns)
        # writer.writeheader() -- Include this if you want a header with the data
        writer.writerow(output)


def plot_results(results):
    trial_numbers = []
    down_speeds = [] 
    up_speeds = []
    for result in results:
        trial_numbers.append(int(result["Trial Number"]))
        down_speeds.append(float(result["Download"]))
        up_speeds.append(float(result["Upload"]))
    pyplot.plot(range(1, (len(trial_numbers) + 1)), down_speeds, label="Down")
    pyplot.plot(range(1, (len(trial_numbers) + 1)), up_speeds, label="Up")
    pyplot.xlabel("Trials - {}".format(result["Date"]))
    pyplot.ylabel("Mbps")
    pyplot.legend()
    # save_prompt = input("Save figure as '{}'? Y/N: ".format(result["Date"]))
    # if(save_prompt.lower() == 'y'):
    #     pyplot.savefig('figures/{}'.format(result["Date"]))
    #     print("Saved!")
    # --include this if you want a save prompt
    pyplot.show()
    

if __name__ == "__main__":
    # num_tests = int(input("Number of tests: "))
    rest_period = int(input("Time between tests (in minutes): "))
    test_speed(rest_period)
    # timer()
