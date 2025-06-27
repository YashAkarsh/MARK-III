from MARK_3 import MARK_III
import time,os

MARK_3=MARK_III()
# avtivating
import requests
import pyttsx3

internet=True
url = "http://www.kite.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("Connected to the Internet")
    
except (requests.ConnectionError, requests.Timeout) as exception:
    internet=False

# Voice Settings
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
engine.setProperty('rate',169)


def speak_2(audio):
    engine.say(audio)
    engine.runAndWait()

if internet==True:
    import speech_recognition as sr
    import pyttsx3
    import datetime

    wake_word='wake up'

    def wake():
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            try:  
                listener=recognizer.listen(source,timeout=2,phrase_time_limit=5)
            except Exception:
                print('An unexpected error occured!')
        try:
            print("recognizing...")
            query=recognizer.recognize_google(listener,language='en-in')
            print(f'User said: {query}')
        except:
            print("sorry I didn't understand!")
            return 'none'
        return query

    def www():
        while True:
            with open('Text_Files\\condition.txt','r') as f:
                data1=f.read()
            if os.path.exists('Text_Files\\activated_BY_key'):
                exit()
                
            if data1=='off' or data1=='sleep' and  not os.path.exists('Text_Files\\activated_BY_key'):
                wake_up=wake()
                if wake_word in wake_up:
                    with open('Text_Files\\condition.txt','w') as g:
                        data2=g.write('on')
                    with open('Text_Files\\activated_BY_word','w') as l:
                        temp_file=l.write('')
                    
                    MARK_3.run()
                    exit()
                
                elif 'bye' in wake_up:
                    with open('Text_Files\\exitornot.txt','w') as h:
                        exn=h.write('exit')
                        time.sleep(3)
                    with open('Text_Files\\exitornot.txt','w') as h:
                        exb=h.write('')

                    exit()
                
                else:
                    pass
            else:
                break

    def wishme_2():
        speak_2('Welcome back sir!; The system is ready to use!')

    if __name__=='__main__':
        wishme_2()
        www()

else:
    speak_2('No internet Connection')