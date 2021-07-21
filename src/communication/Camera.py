import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(3, 2)
amg = adafruit_amg88xx.AMG88XX(i2c)

while True:
    for row in amg.pixels:
        print(["{0:.1f}".format(temp) for temp in row])
        print("")
        print("\n")
        time.sleep(1)