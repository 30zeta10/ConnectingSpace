import pyaudio
import wave
import sys

def playAudio(path):

    wa = wave.open(path, 'rb')
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
