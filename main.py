"""Collect, analyze, and display EMG data."""

import subprocess

print("Connect the Myo armband and sync. When you are ready, press any key.")
input()
subprocess.run("myo-data-capture.cpp")
