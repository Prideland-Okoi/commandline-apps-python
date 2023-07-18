#!/usr/bin/python3
import time


def thermostat(temp, low_temp, high_temp):
    direction = 1
    while True:
        if temp < low_temp:
            print("Min Temp reached. Heating...")
            direction = 1
        elif temp > high_temp:
            print("Max Temp reached. Cooling...")
            direction = -1
        temp += direction
        print(f"Current temperature: {temp}°C")
        time.sleep(1)


thermostat(24, 18, 26)
