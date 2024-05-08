import speech_recognition as sr

def speech_en():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell something!!")
        audio = r.listen(source)
    return(r.recognize_google(audio, language = 'en-GB'))

def speech_tr():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Birşeyler söyle!!")
        audio = r.listen(source)
    return(r.recognize_google(audio, language = 'tr-TR'))

#yazi=speech_tr()
#print(yazi)
   