# Server_Stress_Script
A python script I wrote half a year ago that requests a webpage from a hard-coded server using hard-coded login credentials

The script opens 10 threads that will request the main page of the server 100 times, picking a new random login every time. The threads will print to the console when they are finished, as well as the time it took for the job to complete. The threads will also write more detailed information into their own .txt file, as well as calculating the average time of each request and writing that to the file as well.
I opened the files as an append, and they wrote a header to the file with the datetime of the test start, so that you can compare historical data. It would be tedious and awful, since the data is in one big text file and those are just kind of nasty, but you could do it.
