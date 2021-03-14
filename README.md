# Server_Stress_Script
A python script I wrote half a year ago that requests a webpage from a hard-coded server using hard-coded login credentials

The script opens 10 threads that will request the main page of the server 100 times, picking a new random login every time. The threads will print to the console when they are finished, as well as the time it took for the job to complete. The threads will also write more detailed information into their own .txt file, as well as calculating the average time of each request and writing that to the file as well.
