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


def setBrightness (halt_dunkel_ms, halt_hell_ms, tempo_ms):
	while True:
		for i in range(0,256):
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

def handler(emotion):
	if emotion=='angry':
		angry()
	elif emotion=='suprise':
		suprise()
	elif emotion=='disgust':
		disgust()
	elif emotion=='happy':
		happy()
	elif emotion=='fear':
		fear()
	elif emotion=='sad':
		sad()
	else:
		print 'Dies ist ein ungueltiger Emotion-String\nDas sind gueltige Emotion-Strings:\n (\'angry\', \'suprise\', \'disgust\', \'happy\', \'fear\', \'sad\')'

def angry():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(255,0,0))
	setBrightness2nd(1000.0,250,0.2)

def suprise():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(255, 255, 255))
	setBrightness2nd(1000.0, 250, 0.2)

def disgust():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(75, 0, 0))
	setBrightness2nd(2000.0, 500, 0.2)

def happy():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(255, 255, 255))
	setBrightness(1000.0, 250, 0.2)

def fear():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(255, 0, 0))
	setBrightness(2000.0, 500, 0.2)

def sad():
	strip.setBrightness(0)
	strip.show()
	constantColor(strip,Color(75, 0, 0))
	setBrightness(1000.0, 250, 0.2)

# Main program logic follows:
if __name__ == '__main__':
		# Process arguments
	opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	handler('angry')
#	while True:
#		print ('Color wipe animations.')
#		colorWipe(strip, Color(255, 0, 0))  # Red wipe
#		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#		colorWipe(strip, Color(0, 0, 255))  # Green wipe
#		print ('Theater chase animations.')
#		theaterChase(strip, Color(127, 127, 127))  # White theater chase
#		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
#		print ('Rainbow animations.')
#		rainbow(strip)
#		rainbowCycle(strip)
#		theaterChaseRainbow(strip)
