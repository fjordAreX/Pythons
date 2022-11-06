import os
import time

web = input('enter sites name\n')
time.sleep(1)
if 'https://www.' not in web and '.com' in web:
    os.system('start https://www.'+web)
elif 'https://www.' not in web and '.com' not in web:
    os.system('start https://www.'+web+'.com')
else:
    os.system('start ' + web)

os.startfile('D:\Telegram Desktop\Telegram.exe')
