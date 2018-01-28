"""Collect, analyze, and display EMG data."""

import os
import csv
import fnmatch
import json
import matplotlib
#matplotlib.use("agg")
from matplotlib import pyplot

print("Removing irrelevant files.")
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

assert found, "EMG data not found!"

print("Reading EMG data...")
with open (filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    next(readCSV)
    maximum = 0
    for row in readCSV:
        for i in range(1, 9):
            if int(row[i]) == 127 or int(row[i]) == -127:
                maximum += 1

print("Today's value:", maximum)

print("Deleting EMG file.")
os.remove(filename)

print("Reading results.csv")
data = []
try:
    with open("results.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                data.append([int(i) for i in row])
except FileNotFoundError:
    print("File not found. Creating new...")
    with open("results.csv", "w") as csvfile:
        pass

print("Writing results.csv")
with open("results.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    if not data:
        data.append([1, maximum])
    else:
        data.append([data[-1][0] + 1, maximum])
    for row in data:
        writer.writerow(row)

print("Displaying plot...")
pyplot.plot([row[0] for row in data], [row[1] for row in data], "ro-")
pyplot.show()
pyplot.savefig("result.png")

if len(data) > 30:
    sum = 0
    three_quarter = round(len(data) * 0.75)
    for i in range(three_quarter, len(data)):
        value = data[i][1]
        sum += value

    avg1 = sum / round(len(data) / 4)

    sum = 0
    for i in range(three_quarter):
        value = data[i][1]
        sum += value

    avg2 = sum / three_quarter

    if avg1 < avg2:
        # The user's readings are declining.
        print("\nYour recentEMG readings have been significantly weaker than usual.\n"
              "This may be an early sign of carpal tunnel syndrome. To best avoid "
              "worsening the symptoms, you should begin regularly stretching your "
              "wrist and hands.\n"
              "Would you like to set up repeating reminders to stretch?")
        input("Yes / No [Y]: ")

healthy = {"healthy": True}
with open("data.js", "w+") as outfile:
    outfile.write("var healthy = \"true\";")
