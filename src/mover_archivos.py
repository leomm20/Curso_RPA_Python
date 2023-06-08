import os
from utils import *

"""
Este caso sólo es para realizar una demostración, dado que para mover un archivo, es mejor utilizar otra librería,
por ej.: os.rename()
Este caso aplicaría más para cuando se quiere subir un archivo 1 sharepoint o drive.google
"""

r.hotkey('win', 'r')
sleep()
ruta = os.getcwd() + '\\mover\\temp'
write(ruta)
r.hotkey('enter')
sleep(2)
r.moveTo(r.locateCenterOnScreen('mover/archivo.png'))
pos_dir = r.locateCenterOnScreen('mover/directorio.png')
print(pos_dir)
r.dragTo(pos_dir[0], pos_dir[1], 1)  # hay que darle 1 segundo de tiempo, sino lo suelta antes
sleep()
r.click(pos_dir, clicks=2)
pos = r.locateCenterOnScreen('mover/archivo.png')
r.click(pos, clicks=2)
sleep(2)
r.scroll(-1000)
sleep(2)
r.hotkey('alt', 'f4')
r.hotkey('ctrl', 'z')
sleep()
r.hotkey('alt', 'f4')
r.alert('FIN!')
