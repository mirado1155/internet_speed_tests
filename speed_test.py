import subprocess
import csv
import datetime
import time
import matplotlib


# This function takes the raw, original csv data and extracts only the down / up speeds. Also adds datetime of each trial
def process_csv():
    SPEED_DIVISOR = 100000
    SIGNIFICANT_DIGITS = 2
    with open("speed_test_results.csv", "r") as read_file:
        reader = csv.reader(read_file)
        next(reader)
        with open("down_up_speeds.csv", "w") as write_file:
            writer = csv.writer(write_file)
            for line in reader:
                if (len(line) == 1):
                    writer.writerow([line[0]])
                elif (len(line) > 1):
                    writer.writerow([round((int(line[5]) / SPEED_DIVISOR), SIGNIFICANT_DIGITS), round((int(line[6]) / SPEED_DIVISOR), SIGNIFICANT_DIGITS)])

# This function executes a command which tests internet speed and outputs to a csv file. Set on timer.
def set_continuous_tests():
    NUM_TESTS = 30
    MINUTES_REST = 30
    for test in range(NUM_TESTS):
        curr_time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        with open("speed_test_results.csv", "a") as write_file:
            writer = csv.writer(write_file)
            writer.writerow(["Time: {}".format(curr_time)])
        subprocess.call(["speedtest.exe", "--format=csv", ">>", "speed_test_results.csv"], shell=True)
        print("Test {} conducted: {}".format((test + 1), curr_time))

        if ((test + 1) != NUM_TESTS):
            time.sleep(MINUTES_REST * 60)
        

if __name__ == "__main__":
    set_continuous_tests()
    process_csv()
