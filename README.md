# internet_speed_tests

First, download Ookla speedtest cli from here: https://www.speedtest.net/apps/cli
Make sure to put the contents in the project directory

This application will test your internet speed over specified time intervals, and output all the data to speed_test_results.csv.
Then, it will take JUST the down/up speeds, along with the timestamp of when the tests were taken, and put all that in down_up_speeds.csv.

To run speed_plotter.py, you must have matplotlib installed. This should be fairly simple, and I'll leave it to the user to Google whichever method is easiest for them.
I just used pip.

