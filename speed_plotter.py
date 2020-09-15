import csv
import matplotlib.pyplot as pyplot


def get_and_plot_points():
    x_points = []
    down_points = []
    up_points = []
    with open("down_up_speeds.csv", "r") as read_file:
        reader = csv.reader(read_file)
        for line in reader:
            if (len(line) > 1):
                down_points.append(float(line[0]))
                up_points.append(float(line[1]))
            elif (len(line) == 1):
                x_points.append(line[0])

    pyplot.plot(range(1, (len(down_points) + 1)), down_points, label="Down Speeds")
    pyplot.plot(range(1, (len(down_points) + 1)), up_points, label="Up Speeds")
    pyplot.xlabel("Trials")
    pyplot.ylabel("Mbps")
    pyplot.legend()
    pyplot.show()


if __name__ == "__main__":
    get_and_plot_points()