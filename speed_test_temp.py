from datetime import datetime
import time
import speedtest
import matplotlib.pyplot as pyplot

def timer():
    times = ['00', '11', '30', '45']
    while(True):
        current_time = datetime.now().strftime('%H:%M')
        for quarter in times:
            if (current_time[3:5] == quarter):
                print("It is time {}".format(current_time))
                time.sleep(30)
            elif (quarter == times[3]):
                print("It is not time yet... {}".format(current_time))
        time.sleep(.5)


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
    timer()