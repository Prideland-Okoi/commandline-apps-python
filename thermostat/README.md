# Thermostat
This is a electronic regulator to monitor increase in temperature of the device and regulate temperature

## Script 
|file|description|
|---------|------------------------|
|`thermostat-1.py`|This program takes in the current temperature, the low temperature, and the high temperature as arguments. It also has a direction variable that determines whether the temperature should be increasing or decreasing. The program will continuously check if the current temperature is less than the low temperature or greater than the high temperature. If it is less than the low temperature, it will set the direction to 1, indicating that the temperature should be increasing. If it is greater than the high temperature, it will set the direction to -1, indicating that the temperature should be decreasing. The program will then increment or decrement the temperature based on the direction variable. It will pause for 1 second between each iteration and print out the current temperature.|
