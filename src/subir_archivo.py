import os
from utils import *


r.hotkey('win', 'r')
sleep()
write('chrome.exe https://ps.uci.edu/~franklin/doc/file_upload.html')
sleep()
r.press('enter')
sleep(3)
pos = r.locateCenterOnScreen('subir_archivo/seleccionar_archivo.png')
r.click(pos)
sleep()
ruta_archivo = os.getcwd() + r'\screenshots\ejemplo1.png'
write(ruta_archivo)
r.hotkey('alt', 'a')
sleep()
pos = r.locateCenterOnScreen('subir_archivo/send_file.png')
r.click(pos)
