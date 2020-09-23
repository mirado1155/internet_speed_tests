from datetime import datetime
import time
import speedtest
import csv


def timed_sample_output():
    times = ['00', '15', '30', '45']
    while(True):
        current_time = datetime.now().strftime('%H:%M')
        for quarter in times:
            if (current_time[3:5] == quarter):
                print("It is time {}".format(current_time))
                test_speed(current_time)
                time.sleep(30)
            elif (quarter == times[3]):
                print("It is not time yet... {}".format(current_time))
        time.sleep(1)


def test_speed(curr_time):
    SPEED_DIVISOR = 1000000
    s = speedtest.Speedtest()
    # curr_time = datetime.now()
    download_time = s.download()
    upload_time = s.upload()
    today = datetime.now().date()
    output = {
        "Date":today,
        "Trial Number":(count),
        "Time": curr_time.strftime('%H:%M'),
        "Download":round((download_time / SPEED_DIVISOR), 2),
        "Upload":round((upload_time / SPEED_DIVISOR), 2)
    }
    # results.append(output)
    print("Trial number {} completed".format(count))
    print(output)
    write_to_file(output)

    # plot_results(results)


def write_to_file(output):
    with open('output_file.csv', 'a') as write_file:
        columns = ['Date', 'Trial Number', 'Time', 'Download', 'Upload']
        writer = csv.DictWriter(write_file, fieldnames=columns)
        # writer.writeheader() -- Include this if you want a header with the data
        writer.writerow(output)



    

if __name__ == "__main__":
    timed_sample_output()
