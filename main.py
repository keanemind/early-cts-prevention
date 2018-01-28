"""Collect, analyze, and display EMG data."""

import os
import subprocess
import csv
import fnmatch

print("Connect the Myo armband and sync. \n"
      "Instructions:"
      "1. Press enter to start data capture."
      "2. Clench fist tightly for 2 seconds, then release."
      "3. Repeat 4 more times."
      "4. Close out of the terminal window.")
input()
subprocess.run("myo-data-capture.cpp")

for filename in os.listdir("."):
    if (fnmatch.fnmatch(filename, "accelerometer-*.csv") or
            fnmatch.fnmatch(filename, "gyro-*.csv") or
            fnmatch.fnmatch(filename, "orientation-*.csv") or
            fnmatch.fnmatch(filename, "orientationEuler-*.csv")):

        os.remove(filename)


with open("emg-1517131803.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    next(readCSV)
    maximum = 0

    for row in readCSV:
        print(type(row))
        for i in range(1, 9):
            if int(row[i]) > maximum:
                maximum = int(row[i])

print(max)
