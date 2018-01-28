"""Collect, analyze, and display EMG data."""

import os
import sys
import subprocess
import csv
import fnmatch

for filename in os.listdir("."):
    if (fnmatch.fnmatch(filename, "accelerometer-*.csv") or
            fnmatch.fnmatch(filename, "gyro-*.csv") or
            fnmatch.fnmatch(filename, "orientation-*.csv") or
            fnmatch.fnmatch(filename, "orientationEuler-*.csv")):

        os.remove(filename)

found = False
for filename in os.listdir("."):
    if fnmatch.fnmatch(filename, "emg-*.csv"):
        found = True
        break

assert found, "emg data not found"

with open (filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    next(readCSV)
    maximum = 0
    for row in readCSV:
        for i in range(1, 9):
            if int(row[i]) > maximum:
                maximum = int(row[i])

print(maximum)

os.remove(filename)
