import time
from datetime import datetime, timezone
import pytz
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
big_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

rn = datetime.now()
next_bday = datetime(2022, 1, 11)
ny = datetime(2022, 1, 1)

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    current_day = rn.strftime("%A")
    current_date = rn.strftime("%b %-d")
    current_year = rn.strftime("%Y")
    current_time = rn.strftime("%H:%M")
    current_m = rn.strftime("%p")

    if buttonA.value and buttonB.value:
        x = 10
        y = top + 5
        draw.text((x, y), current_date, font=small_font, fill="#000000")
        y = height - font.getsize(current_day)[1]
        draw.text((x, y), current_day, font=small_font, fill="#000000")
        x = width - font.getsize(current_year)[0]
        y = top + 5
        draw.text((x, y), current_year, font=small_font, fill="#000000")
        y = height - font.getsize(current_m)[1]
        draw.text((x + 5, y), current_m, font=small_font, fill="#000000")

        y = (height - big_font.getsize(current_time)[1])/2
        draw.text(((width - big_font.getsize(current_time)[0])/2, y), current_time, font=big_font, fill="#000000")

    else:
        if buttonB.value and not buttonA.value:  # just button A pressed
            diff = f"new year's in\n{(ny - rn).days} days"
            draw.text(((width - font.getsize(diff)[0])/2 + random.randint(50, 80), (height - font.getsize(diff)[1])/2 - random.randint(10, 30)), diff, font=font, fill="#000000")
        if buttonA.value and not buttonB.value:  # just button B pressed
            diff = f"the next bday's in\n{(next_bday - rn).days} days"
            draw.text(((width - font.getsize(diff)[0])/2 + random.randint(50, 80), (height - font.getsize(diff)[1])/2 - random.randint(10, 30)), diff, font=font, fill="#000000")
        if not buttonA.value and not buttonB.value:  # both pressed
            world = {
            "London": rn.astimezone(pytz.timezone("Europe/London")),
            "Shanghai": rn.astimezone(pytz.timezone("Asia/Shanghai")),
            "LA": rn.astimezone(pytz.timezone("America/Los_Angeles")),
            "New York": rn.astimezone(pytz.timezone("America/New_York")),
            "Rome": rn.astimezone(pytz.timezone("Europe/Rome")),
            "Tokyo": rn.astimezone(pytz.timezone("Asia/Tokyo")),
            "Cairo": rn.astimezone(pytz.timezone("Africa/Cairo"))
            }
            city = random.choice(list(world.keys()))
            local_time = world[city].strftime("%H:%M")
            clk = f"it's {local_time} in {city}"
            draw.text(((width - font.getsize(clk)[0])/2, (height - font.getsize(clk)[1])/2), clk, font=font, fill="#000000")
            time.sleep(2)
    
    disp.image(image, rotation)
    time.sleep(1)

