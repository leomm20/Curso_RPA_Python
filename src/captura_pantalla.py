import pyautogui as r


pantalla = r.screenshot('screenshots/ejemplo1.png')
pantalla_region = r.screenshot('screenshots/ejemplo2.png', region=(28, 110, 480, 400))  # x, y, ancho, alto
