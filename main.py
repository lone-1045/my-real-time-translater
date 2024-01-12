import speech_recognition as sr
import pyttsx3
from googletrans import Translator
def speak(text, speed):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ready")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error:", str(e))
    return None
def translate_text(text, dest_lang='zh-CN'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text
if __name__ == "__main__":
    while True:
        recognized_text = recognize_speech()
        if recognized_text:
            translated_text = translate_text(recognized_text)
            speak(translated_text,150)
            print("Translated:", translated_text)
