import pyaudio
import wave
import sys

if (len(sys.argv) < 2):
    print("No file to play")
    sys.exit(-1)

wa = wave.open(sys.argv[1], 'rb')
play = pyaudio.PyAudio()

stream = play.open(format = play.get_format_from_width(wa.getsampwidth()),
                    channels = wa.getnchannels(),
                    rate = wa.getframerate(),
                    output = True)

daten = wa.readframes(1024)

while daten != '':
    stream.write(daten)
    daten = wa.readframes(1024)

stream.stop_stream()
stream.close()
play.terminate()
