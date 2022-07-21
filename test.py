from st7735 import TFT
from sysfont import sysfont
from machine import Pin, Signal, SoftI2C
from mpu6886 import MPU6886
import time
led = Signal(10, Pin.OUT, invert=True)
led.on()

tft=TFT()
tft.fill(TFT.BLACK)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
sensor = MPU6886(i2c)
time.sleep(0.1)

print(sensor.acceleration)
print(sensor.gyro)
print(sensor.temperature)

