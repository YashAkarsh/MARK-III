import keyboard,time,pyautogui,os
# import volume_control
while True:
    with open('Text_Files\\exitornot.txt','r') as t:
        data1=t.read()
    with open('Text_Files\\condition.txt','r') as t:
        data2=t.read()
    
    # if keyboard.is_pressed('f4'):
    #     volume_control.volume_control_gesture()
    # if os.path.exists('Text_Files\\activated_BY_key'):
    #     pass

    # elif os.path.exists('Text_Files\\activated_BY_key') and os.path.exists('Text_Files\\activated_BY_word'):
    #     try:
    #         os.remove('Text_Files\\activated_BY_key')
    #     except:
    #         os.remove('Text_Files\\activated_BY_Word')
    
    
    # else:
    #     pass
    if data1!='exit' and data2=='on':
        if keyboard.is_pressed('home'):
            with open('Text_Files\\condition.txt','w') as f:
                change=f.write('sleep')
            print('sleep mode activated')

           
        # elif keyboard.is_pressed('f1'):
        #     pyautogui.press('volumemute')
        
        # elif keyboard.is_pressed('f2'):
        #     pyautogui.press('volumedown')
        
        # elif keyboard.is_pressed('f3'):
        #     pyautogui.press('volumeup')
        

        else:
            pass
    else:
        exit()