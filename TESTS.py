# import numpy as np
# import cv2
# import urllib.request
# URL='http://192.168.0.107:8080/shot.jpg' 
# while True:
#     img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
#     image=cv2.imdecode(img_arr,-1)
#     image_resized=cv2.resize(image,(640,460))
#     cv2.imshow("camera",image_resized)
#     a=cv2.waitKey(1)
#     if a==27:
#         break

# cv2.destroyAllWindows()


from twilio.rest import Client
import os

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC66ad3e70a0b0ae108f52f6cbf3079917'
auth_token = 'c87991f43c858afacb5e03625e87d954'
client = Client(account_sid, auth_token)

message = client.calls \
    .create(
         twiml='<Response><Say>A message form Yash Akarsh; for Aditya Singh;    at what time we have to come for group study?;A message form Yash Akarsh; for Aditya Singh;    at what time we have to come for group study?</Say></Response> ',
         from_='+15756399534',
         to='+918425071425'
     )

# import pyautogui,os,time,wikipedia

# with open('tester.docx','w') as f:
#     f.write('')
# os.startfile('tester.docx')
# time.sleep(10)
# answer=wikipedia.summary('Sachin Tendulkar',sentences=100)
# pyautogui.typewrite(answer)
