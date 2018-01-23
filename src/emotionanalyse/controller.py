import SpeechNetSVMMulticlass as spNet
import SVMSentimentAnalysis as ana
import speech_recognition as spR
import datetime
import logging


def analyseaudio(filename):

    r = spR.Recognizer()
    date = datetime.datetime.now().time().isoformat()
    textfile = "./Data/"+str(datetime).replace(":","").replace(".","")+".txt"

    with spR.WavFile(filename) as source:

        audio = r.record(source)
        text = r.recognize_sphinx(audio_data=audio, language="en-US")

        f = open(textfile, "wb")
        f.write(text)
        f.close()

    emotions = spNet.main(filename, False, 20)
    annotation = ana.main(textfile, False, 20)

    positive_emotions = ["happy", "surprise"]
    negative_emotions = ["Angry", "Disgust", "surprise", "sadness", "fear"]
    final_emotion_data = {}

    if(annotation[0] == '1'):
        
        for emotion in positive_emotions:
        
            if(len(emotions.get(emotion)) != 0):
                final_emotions_data.update({emotion: emotions.get(emotion)})

    else:
        
        for emotion in negative_emotions:

            if((emotions.get(emotion)) != None):

                final_emotion_data.update({emotion: emotions.get(emotion)})

    if(len(final_emotion_data) == 0):

        final_emotion_data.update({"Neutral": 1.0})

    final_emotion_data.update({"data": text})
    
    return final_emotion_data



