from MARK_3 import MARK_III
import keyboard
import os
import time
# import volume_control
# from volume_control import gesture_control

# internet
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

if internet==True:
    MARK_3=MARK_III()
    def key():
        while True:

            with open('Text_Files\\condition.txt','r') as f:
                    condit=f.read()
            with open('Text_Files\\exitornot.txt','r') as f:
                    ext=f.read()
                    
            if condit=='off' or condit=='sleep' and not os.path.exists('Text_Files\\activated_BY_word'):
                if keyboard.is_pressed('`'):
                    if os.path.exists('Text_Files\\activated_BY_word'):
                        exit()
                    with open('Text_Files\\condition.txt','w') as g:
                        dat=g.write('on')
                    with open('Text_Files\\activated_BY_key','w') as h:
                        temp_file=h.write('')
                    
                    # os.remove('Text_Files\\activated_BY_key')
                    MARK_3.run()
                    print(MARK_3.switch)
                    keyboard.wait("`")
                
                else:
                    pass
            
            elif ext=='exit':
                exit()
            
            else:
                break

    if __name__=='__main__':
        key()
else:
    exit()