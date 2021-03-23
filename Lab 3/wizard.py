import time
import board
import busio
import digitalio
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

import adafruit_mpr121
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
def font(size):
	return ImageFont.truetype("Garamond.ttf", size)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

num = 0
quotes = [
"i'm already crying for you.",
"start by going for a walk.",
"take a cold shower.",
"your biggest challenge is to avoid becoming dead inside.",
"what would happen if you weren't so scared?",
"maybe you just need a good roll in the hay.",
"get rid of something today.",
"be someone's service animal today.",
"get a plane ticket if you can and go.",
"co-dependence is a temporary fix.",
"you have to believe in something.",
"your nervous energy won't be especially useful today."
]

while True:
	while True:
		draw.rectangle((0, 0, width, height), outline=0, fill="#003300")

		if mpr121.touched():
			for i in range(12):
				if mpr121.is_touched(i):
					num = i
			break

		else:
			draw.text((15, 30), "tell me your birthday\nand pick a number", font=font(26), fill="#CD5C5C")

		disp.image(image, rotation)
		time.sleep(0.25)

	head = "your day at a glance"
	y = top
	draw.text(((width - font(20).getsize(head)[0])/2, y), head, font=font(20), fill="#000000")

	quote = quotes[random.randint(0, 11)]

	lines = textwrap.wrap(quote, width=20)

	x_text = 20
	if len(lines) == 1:
		x_text = 25
		y_text = 50
	elif len(lines) == 2:
		y_text = 35
	elif len(lines) == 3:
		y_text = 28
	else:
		y_text = 20
	
	for line in lines:
		draw.text((x_text, y_text), line, font=font(25), fill="#CD5C5C")
		y_text += 22

	disp.image(image, rotation)
	os.system(f"espeak '{quote}'")
	time.sleep(5)


