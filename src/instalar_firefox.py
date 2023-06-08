from utils import *


r.hotkey('win', 'r')
sleep()
write('chrome.exe https://www.mozilla.org/es-AR/firefox/new/')
sleep()
r.press('enter')
sleep(3)
r.click('firefox/01_descargar.png')
sleep(8)
write(r'c:\users\maggiotl\Downloads\firefox_installer.exe')
sleep()
r.hotkey('alt', 'g')
sleep(7)
r.click('firefox/firefox_installer.png')
r.alert('Fin del script!\n'
        'Esta es sólo una muestra, por lo tanto, luego deberías'
        'agregar los pasos para la instalación real')
