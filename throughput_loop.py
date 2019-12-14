#!/bin/python
# ER-X Throughput Measurement - Conor Walsh 2018 (Updated 2019)
import sys
import paramiko
import re
import time
import atexit

# Name of interface you want to monitor usually your WAN interface (space to differentiate from VLANs)
erinterface = "eth0 "
# Time between 1st and 2nd measurement
sleeptime = 0
# Time between throughput measurements
cycletime = 30
# Router Username
user = "username"
# Router Password
passw = "password"
# Router IP
routerip = "192.168.1.1"

# Setup the SSH connection
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(username=user, password=passw, hostname=routerip)
except:
    print("SSH Connect Error")
    exit()

# Command used to get the Byte Stats
command = ('''vbash -ic "show interfaces counters | grep '%s'"''' % (erinterface))

# Record number of measurements
cycles = 1


# Exit handler to close SSH connection
def exit_handler():
    # Close SSH
    ssh.close()
    print("\nBye...")


atexit.register(exit_handler)

while True:

    print("==============================")
    print("        Measurement " + str(cycles))
    print("==============================\n")

    # Issue the SSH command
    try:
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    except:
        print("SSH Command Error")
        ssh.close()
        exit()

    # Record the first timestamp
    time1 = time.time()

    print("Measure 1:")
    # Read the Byte info
    lines = ssh_stdout.readlines()
    out = ""
    for line in lines:
        out = line

    # Split the Byte info
    s = re.sub("\s+", ",", out.strip())
    data = s.split(',')

    # Get RX TX values
    rxb1 = int(data[2])
    txb1 = int(data[4])

    print("Rx: " + str(rxb1) + "B Tx: " + str(txb1) + "B\n")

    # Sleep before 2nd measurement
    time.sleep(sleeptime)

    try:
        ssh_stdin1, ssh_stdout1, ssh_stderr1 = ssh.exec_command(command)
    except:
        print("SSH Command Error")
        ssh.close()
        exit()

    time2 = time.time()

    print("Measure 2:")
    lines = ssh_stdout1.readlines()
    out = ""
    for line in lines:
        out = line

    s = re.sub("\s+", ",", out.strip())
    data = s.split(',')
    rxb2 = int(data[2])
    txb2 = int(data[4])

    print("Rx: " + str(rxb2) + "B Tx: " + str(txb2) + "B\n")

    # Get measurement intervals
    interval = time2 - time1

    print("Interval:", round(interval, 3), "seconds\n")

    print("Throughput:")

    # Calculate Throughput in kbps
    rxbs = (((rxb2 - rxb1) / interval) * 8) / 1000
    txbs = (((txb2 - txb1) / interval) * 8) / 1000

    # Format output of RX
    rxbs_s = ""
    if (rxbs >= 1000):
        rxbs_s = str(round((rxbs / 1000), 2)) + "Mbps"
    else:
        rxbs_s = str(round(rxbs, 2)) + "kbps"

    # Format output of TX
    txbs_s = ""
    if (txbs >= 1000):
        txbs_s = str(round((txbs / 1000), 2)) + "Mbps"
    else:
        txbs_s = str(round(txbs, 2)) + "kbps"

    print("Download: %s Upload: %s\n" % (rxbs_s, txbs_s))

    # Sleep before next cycle
    for remaining in range(cycletime, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds until next measurement".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rStarting next measurement                \n\n")

    # Increment Cycles
    cycles += 1
