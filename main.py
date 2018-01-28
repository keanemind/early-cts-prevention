"""Collect, analyze, and display EMG data."""

import subprocess
import csv 

print("Connect the Myo armband and sync. When you are ready, press any key.")
input()
subprocess.run("myo-data-capture.cpp")

with open("emg-1517131803.csv") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=",")
	next(readCSV)
	max = 0

	for row in readCSV:
		print(type(row))
		for i in range(1, 9):
			if int(row[i]) > max:
				max = int(row[i])			

print(max)
