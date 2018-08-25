# EdgeOS Throughput Measurement Tools
Python scripts for measuring throughput on a ubiquiti router (running EdgeOS).<br/>
NOTE: This script does not perform a speedtest, it returns the throughput of the router which is how much data is moving up or down through the router at that time.<br/>
There are two versions of the script one that runs once (throughput.py) and one that runs until stopped (throughput_loop.py).

# Requirements
These scripts require the paramiko python module for ssh.<br/>
>pip install paramiko

# Setup
The scripts require 5 values to be set before the script can be used:
1. Set the name of the interface you want to monitor: erinterface = "eth0 "
2. Set the time between the 1st and 2nd measurement: sleeptime = 0
3. Set the username of the router: user = "username"
4. Set the password of the router: passw = "password"
5. Set the IP of the router: routerip = "192.168.1.1"<br/>
The loop script also requires the time between loops: cycletime = 30

# Single Run Script (throughput.py)
The single run script will run once and then exit.<br/>
An example of the script output can be seen below.<br/>
<img src="https://github.com/conorwalsh/EdgeOS-Throughput-Measure/blob/master/pictures/non-loop%20measurement.PNG" />

# Loop Script (throughput_loop.py)
The loop script will run until exited (CTRL+C).<br/>
An example of the script output can be seen below.<br/>
<img src="https://github.com/conorwalsh/EdgeOS-Throughput-Measure/blob/master/pictures/loop%20measurement.PNG" />

License (MIT)
------
Copyright (c) 2018 Conor Walsh 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Thanks
------

Thank you for taking the time to look at this project I hope that it is of use to you,<br/>
<img src="http://conorwalsh.net/sig.png" /><br/>
Conor Walsh.
