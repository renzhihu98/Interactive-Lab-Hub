import time
import subprocess
import digitalio
import board
import random
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    current_date = time.strftime("%m/%d/%Y")
    current_time = time.strftime("%H:%M:%S")

    if buttonA.value and buttonB.value:
        txt = "CLICK THE BUTTONS"
        draw.text(((width - font.getsize(txt)[0])/2, (height - font.getsize(txt)[1])/2), txt, font=font, fill="#FFFF00")
    else:
        if buttonB.value and not buttonA.value:  # just button A pressed
            date = f"Today is\n{current_date}"
            draw.text(((width - font.getsize(date)[0])/2, (height - font.getsize(date)[1])/2), date, font=font, fill="#FFFF00")
        if buttonA.value and not buttonB.value:  # just button B pressed
            c_time = f"Now is\n{current_time}"
            draw.text(((width - font.getsize(c_time)[0])/2, (height - font.getsize(c_time)[1])/2), c_time, font=font, fill="#FFFF00")
        if not buttonA.value and not buttonB.value:  # none pressed
            rn = f"{current_date} {current_time}"
            draw.text(((width - font.getsize(rn)[0])/2, (height - font.getsize(rn)[1])/2), rn, font=font, fill="#FFFF00")

    disp.image(image, rotation)
    time.sleep(0.5)