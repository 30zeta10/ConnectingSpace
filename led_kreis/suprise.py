import time

from neopixel import *

import argparse
import signal
import sys
def signal_handler(signal, frame):
		colorWipe(strip, Color(0,0,0))
		sys.exit(0)

def opt_parse():
		parser = argparse.ArgumentParser()
		parser.add_argument('-c', action='store_true', help='clear the display on exit')
		args = parser.parse_args()
		if args.c:
				signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10     # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



# Define functions which animate LEDs in various ways.

def constantColor (strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()

def setBrightness2nd(halt_dunkel_ms, halt_hell_ms, tempo_ms):
	while True:
		for i in range(1,256):
			print ('Brightness'+str(i))
			strip.setBrightness(i)
			strip.show()
			time.sleep(tempo_ms/1000.0)
			if i==255:
				time.sleep(halt_hell_ms/1000.0)
				for i in range(254,49,-1):
					print ('Brightness'+str(i))
					strip.setBrightness(i)
					strip.show()
					time.sleep(tempo_ms/1000.0)
					if i==50:
						for i in range(51,256):
							print ('Brightness'+str(i))
							strip.setBrightness(i)
							strip.show()
							time.sleep(tempo_ms/1000.0)
							if i==255:
								time.sleep(halt_hell_ms/1000.0)
								for i in range(254,-1,-1):
									print ('Brightness'+str(i))
									strip.setBrightness(i)
									strip.show()
									time.sleep(tempo_ms/1000.0)
								time.sleep(halt_dunkel_ms/1000.0)

def suprise():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(255, 255, 255))
	setBrightness2nd(1000.0, 250, 0.2)

if __name__ == '__main__':
		# Process arguments
	opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	suprise()
