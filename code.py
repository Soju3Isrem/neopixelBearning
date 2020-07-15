import analogio
import board
import time
import neopixel

PIXEL_PIN = board.D2

ORDER = neopixel.RGB  
COLOR = (0, 255, 0) 
COLORB = (0, 0, 255)  
CLEAR = (0, 0, 0) 

pixel = neopixel.NeoPixel(PIXEL_PIN, 16, pixel_order=ORDER)

# Analog inputs for each ADXL335 axis.
x_axis = analogio.AnalogIn(board.A1)
y_axis = analogio.AnalogIn(board.A2)
z_axis = analogio.AnalogIn(board.A3)

 # Convert analog values to gravities.
def accel_value(axis):
    val = axis.value / 65535
    val -= 0.5
    return val * 3.0
i =0
while True:
    x = accel_value(x_axis)
    y = accel_value(y_axis)
    z = accel_value(z_axis)
    if x>y:
        pixel[i] = CLEAR
        if i <16:
            i=i+1
        if i == 16:
            i = 0 
            pass
        pixel[i] = COLOR
    if y>x:
        pixel[i] =  CLEAR
        if i == -1:
            i=15
            pass
        if  i>-1:
            i=i-1 
        pixel[i] = COLORB
    time.sleep(.2)
