import sys
import pyaudio
import wave 
import os

import controller as controll
import play as pl
import record as rec
import publish as pub

topic = '/voice'
wavFile = []
keys = []

rec.recordAudio()
emotion = controll.analyseaudio('./voice.wav')

for key in emotion:
    keys.append(key)

msg = str(keys[0])
pub.publishMqtt(msg)


