class MARK_III():
    switch='off'

    def run(self):
        import pyttsx3
        import pyaudio
        import speech_recognition as sr
        import time
        import datetime
        import random
        import webbrowser
        import os
        import pywhatkit
        import pyautogui
        import wolframalpha
        from playsound import playsound
        import urllib.request
        import cv2
        import numpy as np


        # wolframalpha
        app=wolframalpha.Client('KGQWTR-73Q5WR5JGY')
        
        # variable
        name='Mark Three'
        age='25'
        Gender='Male'
        user_name='Yash'
        wake_word='activate'
        sng_words='songs','music'
        fld_words='folder','directory','file','files'
        wishing_words='good morning','good evening','good night','good afternoon'
        appreciate_words='good','nice','god','cool','wow'
        names='om','home','ibrahim','nikhil'
        contacts={'om':'+917039910873',
                'home':'+917039910873',
                'ibrahim':'+919324104426',
                'nikhil':'+919323852881'}

        # key_sleep
        os.startfile('Text_Files\\sleeper.pyw')

        # Voice Settings
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        # engine.setProperty('voice',"Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_Cortana")
        engine.setProperty('rate',169)

        # main functions
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        def wishme():
            greeting_time=int(datetime.datetime.now().hour)
            current_time=datetime.datetime.now()
            current_time=current_time.strftime('%I:%M')
            if greeting_time>=12 and greeting_time<=16:
                speak(f'Good After noon sir!, the time is {current_time} pm')

            elif greeting_time<12 and greeting_time>=3:
                speak(f'Good morning sir!, the time is {current_time} am')

            else:
                speak(f'Good evening sir!, the time is {current_time} pm')
        def command():
            recognizer=sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening...')
                speak('Listening..')
                try:
                    sleep_checker()
                    recognizer.pause_threshold=1
                    listener=recognizer.listen(source,timeout=3,phrase_time_limit=5)
                    sleep_checker()
                    # recognizer.energy_threshold=190     
                except sr.WaitTimeoutError:
                    print('error!')
            try:
                print("recognizing...")
                sleep_checker()
                query=recognizer.recognize_google(listener,language='en-in')
                sleep_checker()
                print(f'User said: {query}')

            except Exception:
                print("sorry I didn't understand!")
                return 'None'
            return query


        def other_command():
            recognizer_2=sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening..')
                listener_2=recognizer_2.listen(source,timeout=2,phrase_time_limit=5)
            try:
                query_2=recognizer_2.recognize_google(listener_2,language='en-in')
                print(f'Requested: {query_2}')
                # speak(f'User said: {query}')
            except:
                speak("sorry I didn't understand!")
                return 'none'
            return query_2

        # other functions
        def open_google():
            speak('Oppening google')
            os.startfile('chrome.exe')

        def open_notepad():
            speak('Oppening notepad')
            os.startfile('notepad.exe')

        def open_cmd():
            speak('Oppening command prompt')
            os.startfile('cmd.exe')

        def open_explorer():
            speak('Oppening explorer')
            os.startfile('explorer.exe')

        def open_YouTube():
            speak('Oppening YouTube')
            webbrowser.open('https://www.youtube.com/')

        def open_google_meet():
            speak('Oppening google meet')
            webbrowser.open('https://meet.google.com/')

        def open_gmail():
            speak('Oppening gmail')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        def search_google(what):
            # what=what.replace('search')
            speak(f'Searching {what} on google')
            pywhatkit.search(what)

        def search_youtube(a):
            # speak(f'searching {a} in YouTube')
            pywhatkit.playonyt(a)


        def open_otherfiles(file):
            speak(f'opening {file}')
            pyautogui.press('win')
            pyautogui.typewrite(file)
            time.sleep(1)
            pyautogui.press('enter') 

        def calc(nums):
                try:
                    resp=app.query(nums)
                    speak(f'Your answer is {next(resp.results).text}')
                except Exception:
                    speak('Sorry no internet connection')

        def temp(pl):
            speak('getting the temperature')
            try:
                resp=app.query(pl)
                speak(f'The temperature is {next(resp.results).text}')
            except Exception:
                speak('Sorry no internet connection')

        def sleep_checker():
            with open('Text_Files\\condition.txt','r') as L:
                d=L.read()
            if d=='sleep':
                with open('Text_Files\\condition.txt','w') as f:
                    dela=f.write('off') 
                speak('going to sleep mode.')
                os.startfile('sleep_mode.pyw')
                exit()
            else:
                pass
        
        def dif_wish():
            speak('Always here for you sir!;')
        
        # brain
        choose_wish=dif_wish,wishme
        random.choice(choose_wish)()
        
        # deleting temperory file
        try:
            os.remove('Text_Files\\activated_BY_word')
        except Exception:
            os.remove('Text_Files\\activated_BY_key')

        while(True):
            sleep_checker()
            user = command().lower()
            # chatbot
            if 'search' in user:
                user = user.replace('search', '')
                if 'on google' in user:
                    user=user.replace('on google','')
                elif 'in google' in user:
                    user=user.replace('in google','')
                search_google(user)

            elif 'repeat' in user:
                user=user.replace('repeat','')
                variate6='Ok','alright!'
                speak(random.choice(variate6))
                speak(user)
            
            elif 'message' in user:
                speak('to whom should I send the message?')
                cntc=other_command().lower()
                print(cntc)
                number=contacts.get(cntc)
                print(number)
                variate1='alright','okay'
                speak(random.choice(variate1))
                try:
                    speak('What should be the message?')
                    msg_inp=other_command()
                    greeting_hour=int(datetime.datetime.now().hour)
                    greeting_minute=int(datetime.datetime.now().minute)
                    speak('Your message will be sent in next 1 minute')
                    pywhatkit.sendwhatmsg(number,msg_inp,greeting_hour,greeting_minute+1)
                    speak('message sent!')
                except Exception:
                    speak('no such contact')

            elif 'hello' in user or user.startswith('hai') or 'hi' in user or 'hey' in user or 'whats up' in user:
                hi_varitaion = 'Hello there!', 'Hi there','Hi!!'
                ans_hello = random.choice(hi_varitaion)
                speak(ans_hello)

            # elif 'how ' in user and 'are you' in user and 'doing' in user:
            #     speak('I am fine!')
            
            elif "say hello to" in user:
                user=user.replace("say hello to "," ")
                hello_variations1=[f"Hi {user}", f"Hello{user}"]
                speak(random.choice(hello_variations1))
            
            elif 'your name' in user:
                name_variations=f'My name is {name}',f'I am {name}\n your personal assistant',f'I am {name}'
                ans_name=random.choice(name_variations)
                speak(ans_name)
            
            elif 'creator' in user or 'created you' in user or 'developed you' in user or 'your developer' in user:
                creator_variations= "Yash Akarsh created me", "I was created by Yash Akarsh", 'I was developed by Yash Akarsh',"Yash Akarsh is my developer" 
                ans_creator=random.choice(creator_variations)
                speak(ans_creator)

            elif 'how' in user and 'you' in user:
                how_are_variations='I am totally fine; Thank You', 'I am fine\n Thank You for asking'
                ans_areyou=random.choice(how_are_variations)
                speak(ans_areyou)
            
            elif 'thank you' in user or 'thanks' in user:
                variate2='welcome!','Your welcome sir'
                speak(random.choice(variate2))
        
            elif 'who' in user and 'you' in user:
                variate3=f'I am {name}\n Your personal assistant,\t how may I help you?',f'Hello there!; I am {name}'
                speak(random.choice(variate3))
            
            elif 'my name' in user:
                variate4=f'according to the details\t your name is {user_name}',f'Your name is {user_name}'
                speak(random.choice(variate4))

            elif 'how to' in user:
                search_google(user)

            elif 'your age' in user:
                variate7=f'My age is {age}',f'I am {age}'
                speak(f'My age is {age}')
            
            elif 'f***' in user or 'hell' in user:
                f_variations='AAAh!; I cannot hear that',"Please dont say it again!","I cannot not tolerate that"
                f_ans=random.choice(f_variations)
                speak(f_ans)
            
            elif 'love' in user:
                love_variations='I can be your best friend',"I am just a machine","I am an artifitial intelligence and not a human so i cannot love"
                love_ans=random.choice(f_variations)
                speak(love_ans)

            elif '**' in user:
                speak('moving on!')

            elif user in wishing_words:
                if 'good morning' in user:
                    speak('Good Morning sir!')
                elif 'good afternoon' in user:
                    speak('Good afternoon sir!')
                elif 'good evening' in user:
                    speak('Good evening sir!')
                elif 'good night' in user:
                    speak('Good night sir')


            elif user in appreciate_words:
                variate5='Thanks!',''
                speak(random.choice(variate5))
    
            # tasks
            
            elif 'open google' in user:
                open_google()
            
            elif 'open notepad' in user:
                open_notepad()
            
            elif 'open cmd' in user:
                open_cmd()
            
            elif 'open youtube' in user:
                open_YouTube()

            elif 'open meet' in user:
                open_google_meet()
            
            elif 'open gmail' in user:
                open_gmail()
            
            elif 'on youtube' in user:
                try:
                    user=user.replace("on youtube"," ")
                    user=user.replace("search", " ")
                    
                    if "search" in user.lower():
                        user=user.replace("search", "searching")
                    elif "user" in user.lower():
                        user=user.replace("play", "Playing")
                    speak(f"Playing {user} on YouTube")
                except:
                    pass
                search_youtube(user)

            elif 'play' in user and 'music' in user or 'play' in user and 'songs' in user:
                speak('Alright!')
                path_songs="F:\Yash\Songs"
                sngs=os.listdir(path_songs)
                own=random.choice(sngs)
                os.startfile(os.path.join(path_songs,own))

            elif 'open' in user and 'songs' in user or 'songs' in user or 'music' in user or 'open' in user and 'music' in user:
                speak('Opening Songs folder')
                path_s="F:\Yash\Songs"
                os.startfile(path_s)

            elif 'open' in user and 'school' in user or 'ryan' in user or 'topper' in user:
                speak('Alright!; opening school os')
                webbrowser.open('https://ryangroup.toppr.school/join-classroom/')
            
            elif 'open' in user and 'whatsapp' in user:
                speak('Opening Whatsapp')
                os.startfile("C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk")

            elif 'open' in user:
                user=user.replace('open', '')
                open_otherfiles(user)
            
            elif 'close google' in user or 'close chrome' in user:
                speak('Ok')
                os.system('taskkill /f /im chrome.exe')

            elif 'close notepad' in user:
                try:
                    speak('Ok')
                    os.system('taskkill /f /im notepad.exe')
                except:
                    speak("It's not oppened!")

            elif 'close' in user:
                user=user.replace('close', '')
                try:
                    speak('Ok')
                    os.system(f"taskkill /f /im {user}.exe")
                except:
                    speak("It's not oppened!")
            
            elif 'calculate' in user or 'calculation' in user:
                if 'calculate' in user:
                    user=user.replace('calculate', '')
                elif 'calculation' in user:
                    user=user.replace('calculation','')
            
                elif 'into' in user:
                    user=user.replace('into','x')
                calc(user)

            elif 'temperature' in user:
                temp(user)

            elif 'create' in user and 'folder' in user:
                speak('Alright! what should be the name of the file?')
                name_file=other_command()
                os.chdir("C:\\Users\\ADMIN\\Desktop\\Yash")
                os.mkdir(name_file)
                speak('done')
            
            elif 'project' in user:
                speak('Ok sir!\n creating a project')
                speak("What should be the project's name?")
                name_project=other_command()
                speak('Ok')
                os.chdir("C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects")
                os.mkdir(name_project)
                os.chdir(f"C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects\\{name_project}")
                with open(f'{name_project}.py', 'w') as f:
                    st_wr=f.write('')
                os.startfile(f'C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects\\{name_project}\\{name_project}.py')
                os.chdir(f"C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects\\MARK I")
                speak('done!')
                continue
            
            elif 'check' in user and 'mail' in user:
                speak('Checking gmails...')
                open_gmail()

            elif 'check' in user and 'messages' in user:
                speak('checking whatsapp messages...')
                path_for_whts='C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp'
                os.startfile(path_for_whts)

            elif 'bye' in user or 'bike' in user:
                speak('Bye sir have a good day!')
                with open('Text_Files\\condition.txt','w') as d:
                    data2=d.write('off')
                with open('Text_Files\\exitornot.txt','w') as d:
                    data2=d.write('exit')
                time.sleep(5)
                with open('Text_Files\\exitornot.txt','w') as d:
                    data8=d.write('')
                exit()
            
            elif 'shutdown' in user:
                speak('shutting down the pc')
                os.system('shutdown /s /t 7')
                time.sleep(4)
                exit()
            
            elif 'sing' in user or 'sin' in user:
                speak('As your wish.')
                path_songs_2="F:\Yash\Songs"
                os.chdir("F:\Yash\Songs")
                sngs_2=os.listdir(path_songs_2)
                # own_2=random.choice(sngs_2)
                # a_1='Aasan Nahin Yahan.mp3','Milne Hai Mujhse Aayi.mp3','Sunn Raha Hai (Male).mp3','Chahun Main Ya Naa.mp3','Bhula Dena.mp3'
                a_2=random.choice(sngs_2)
                playsound(a_2)

            elif 'cancel' in user:
                pywhatkit.cancelShutdown()
            
            elif 'restart' in user:
                speak('restarting the pc')
                os.system('shutdown /r /t 7')
                time.sleep(4)
                exit()
            
            elif 'cancel restart' in user:
                pywhatkit.cancelShutdown()

            
            elif 'mode' in user or 'mod' in user:
                speak('Ok\n going to sleep')
                with open("Text_Files\\condition.txt",'w') as f:
                    data=f.write('off')
                try:
                    os.remove('Text_Files\\activated_BY_key')
                except Exception:
                    os.remove('Text_Files\\activated_BY_Word')
                    
                os.startfile('sleep_mode.pyw')
                exit()
            
            elif 'decrease' in user and 'volume' in user or 'lower' in user and 'volume' in user:
                pyautogui.press('volumedown')
            
            elif 'increase' in user and 'volume' in user:
                pyautogui.press('volumeup')
            
            elif 'mute' in user:
                pyautogui.press('volumemute')
            
            elif 'unmute' in user:
                pyautogui.press('volumeunmute')
            
            elif 'time' in user:
                current_time_2=datetime.datetime.now()
                current_time_2=current_time_2.strftime('%I:%M')
                speak(f"The time is {current_time_2} ")

            elif 'date' in user:
                speak(f"Today's date is {datetime.datetime.date(datetime.datetime.now())}")

            elif 'mobile' in user and 'camera' in user or 'phone' in user and 'camera' in user:
                speak('ok')
                URL='http://192.168.0.107:8080/shot.jpg' 
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    image=cv2.imdecode(img_arr,-1)
                    image_resized=cv2.resize(image,(640,460))
                    cv2.imshow("camera",image_resized)
                    a=cv2.waitKey(1)
                    if a==27:
                        break

                cv2.destroyAllWindows()


            # elif 'artificial' in user:
            #     speak('Ok sir!\n creating a project')
            #     speak("What should be the project's name?")
            #     with open('MARK_2.py','r') as f:
            #         data=f.read()
            #     name_project_2=other_command()
            #     speak('Ok')
            #     os.chdir("C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects")
            #     os.mkdir(name_project_2)
            #     os.chdir(f"C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects\\{name_project_2}")
            #     with open(f'{name_project_2}.py', 'w') as f:
            #         st_wr=f.write(data)
            #     os.startfile(f'C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects\\{name_project_2}\\{name_project_2}.py')
                
            #     os.chdir(f"C:\\Users\\ADMIN\\Desktop\\Yash\\Programming\\Python\\Projects\\MARK I")
            #     speak('done!')
            #     continue

            else:
                pass

