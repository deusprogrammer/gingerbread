from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from datetime import datetime

import time
import math

MS_PER_DAY = 1000 * 60 * 60 * 24
MS_PER_HOUR = 1000 * 60 * 60
MS_PER_MINUTE = 1000 * 60
MS_PER_SECOND = 1000

def getTimeString(ms):
    days = math.floor(ms / MS_PER_DAY)
    hours = math.floor((ms % MS_PER_DAY) / MS_PER_HOUR)   
    minutes = math.floor((ms % MS_PER_HOUR) / MS_PER_MINUTE) 
    seconds = math.floor((ms % MS_PER_MINUTE) / MS_PER_SECOND) 
    return f'{days:3} d {hours:2} h {minutes:2} m {seconds:2} s' 

serial = spi(device=0, port=0) 
device = ssd1309(serial)

xmasTimestamp = datetime.strptime('25.12.2023 00:00:00', "%d.%m.%Y %H:%M:%S")
xmasMs = xmasTimestamp.timestamp() * 1000 

while True:
    with canvas(device) as draw:
        currTimeMs = time.time() * 1000 - MS_PER_HOUR * 6
        msToXMas = xmasMs - currTimeMs
        timeStr = getTimeString(msToXMas)
        print(timeStr)
        draw.text((5, 20), " Christmas Countdown ", fill="white")
        draw.text((15, 40), timeStr, fill="white")
        time.sleep(1) 
