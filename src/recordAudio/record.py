import pyaudio
import wave

audio_rate = 44100
audio_piece = 1024
audio_recordedTime = 5

pl = pyaudio.PyAudio()

stream = pl.open(format = pyaudio.paInt16,
                    channels = 2,
                    rate = audio_rate,
                    input = True,
                    frames_per_buffer = audio_piece)

frames = []

for i in range(0, int(audio_rate/audio_piece * audio_recordedTime)):

    daten = stream.read(audio_piece)
    frames.append(daten)

stream.stop_stream()
stream.close()
pl.terminate()

wa = wave.open("output.wav", 'wb')
wa.setnchannels(2)
wa.setsampwidth(pl.get_sample_size(pyaudio.paInt16))
wa.setframerate(audio_rate)
wa.writeframes(b''.join(frames))
wa.close()
