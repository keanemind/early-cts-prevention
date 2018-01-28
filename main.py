"""Collect, analyze, and display EMG data."""

import subprocess
import csv
import os

print("Connect the Myo armband and sync. \n"
      "Instructions:"
      "1. Press enter to start data capture."
      "2. Clench fist tightly for 2 seconds, then release."
      "3. Repeat 4 more times."
      "4. Close out of the terminal window.")
input()
subprocess.run("myo-data-capture.cpp")


def find(name, path):
  for root, dirs, files in os.walk(path):
    for file in files:
      if name in file[0:3]:
        return os.path.join(root, file)

emgPath = find("emg", "/Users/Bala/Desktop/dataset")

with open (emgPath) as csvfile:
  readCSV = csv.reader(csvfile, delimiter=",")
  next(readCSV)
  max = 0
  for row in readCSV:
    for i in range(1, 9):
      if int(row[i]) > max:
        max = int(row[i])     

print(max)

os.remove(emgPath)
