from gpiozero import CPUTemperature
import time

i = 0
total = 0
while i < 10:
	i+=1
	cpuC = CPUTemperature()
	cpuF = cpuC.temperature / 5 * 9 + 32
	print(cpuF)
	total += cpuF
	time.sleep(.1)
print("Average: " + str(total / i) + " F")