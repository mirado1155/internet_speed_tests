from datetime import datetime
import time
import speedtest
import csv
import matplotlib.pyplot as pyplot

def test_speed(num_tests, rest_period):
    SPEED_DIVISOR = 1000000
    s = speedtest.Speedtest()
    results = []
    for test in range(num_tests):
        curr_time = datetime.now()
        download_time = s.download()
        upload_time = s.upload()
        output = {
            "Date":datetime.now().date(),
            "Trial Number":test,
            "Time": curr_time.strftime('%I:%M'),
            "Download":round((download_time / SPEED_DIVISOR), 2),
            "Upload":round((upload_time / SPEED_DIVISOR), 2)
        }
        results.append(output)
        print("Trial number {} completed".format(test + 1))
        print(output)
        time.sleep(rest_period * 60)
    save_results(results)
    plot_results(results)

def save_results(results):
    columns = ['Date', 'Trial Number', 'Time', 'Download', 'Upload']
    filename = "speed_test_results.csv"
    with open(filename, "a") as write_file:
        writer = csv.DictWriter(write_file, fieldnames = columns)
        writer.writeheader()
        writer.writerows(results)


def plot_results(results):
    trial_numbers, down_speeds, up_speeds = []
    for result in results:
        trial_numbers.append(int(result["Trial Number"]))
        down_speeds.append(float(result["Download"]))
        up_speeds.append(float(result["Upload"]))
    pyplot.plot(range(1, (len(trial_numbers) + 1)), down_speeds, label="Down")
    pyplot.plot(range(1, (len(trial_numbers) + 1)), up_speeds, label="Up")
    pyplot.xlabel("Trials - {}".format(result["Date"]))
    pyplot.ylabel("Mbps")
    pyplot.legend()
    pyplot.savefig('figures/{}'.format(result["Date"]))
    pyplot.show()
    

if __name__ == "__main__":
    num_tests = int(input("Number of tests: "))
    rest_period = int(input("Time between tests (in minutes): "))
    test_speed(num_tests, rest_period)
