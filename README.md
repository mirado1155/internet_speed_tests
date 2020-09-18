# internet_speed_tests

This application will periodically test your internet down/up speed, output it to a .csv file, and plot & save a graph. 

First, it will ask you how many separate trials you would like to conduct. Then it will ask you how long you'd like to wait between each trial.
Keep in mind, it will not be perfect since the program will add the user's input time to the time it actually takes to conduct the tests. This
is an issue that I hope to resolve in the future.

Once the user has entered in the number of trials and the delay between them, the tests will begin. There is terminal output which will show some
information about each test. Once all of the tests are finished, all of the data will be output to a .csv file. I am currently working on a way
to make it so that it writes to the .csv as it goes, in case there are any issues and the data won't all be lost.

Finally, this program will take all that gathered data and put it on a simple graph.
