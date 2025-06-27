import os

with open('Text_Files\\condition.txt','w') as f:
    f.write('off')

os.startfile('key_detection.pyw')
os.startfile('word_detection.pyw')