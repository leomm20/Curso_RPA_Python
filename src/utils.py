import pyautogui as r
import time
import pyperclip as c

"""
Para ver en dónde está el x, y del mouse, y el color RGB de fondo:
cmd
python
import pyautogui
while True:
    pyautogui.displayMousePosition()

Siempre que se pueda, usar teclas de atajo, o detección de imagen (sobre una imagen ya guardada)
"""


def write(text: str):
    """
    Se crea esta función utilizando pyperclip en lugar de la función write de pyautogui, dado que esta última
    no acepta caracteres latinos como ser "¿", tildes, "ñ"
    :param text: cadena de texto que se quiera escribir
    """
    c.copy(text)
    r.hotkey('ctrl', 'v')


def sleep(time_secs: float = 1.0):
    """
    Se utiliza para generar una pausa, dando tiempo al sistema a que finalice algún proceso (ej. cargar una página web)
    :param time_secs: 1 segundo como default
    """
    time.sleep(time_secs)


def pn(posicion_referencia_x: int, posicion_referencia_y: int) -> tuple:

    posicion_referencia = posicion_referencia_x, posicion_referencia_y
    # Obtener la posición relativa del ícono en una resolución de referencia
    resolucion_referencia = (1920, 1080)

    # Obtener la resolución actual
    resolucion_actual = r.size()

    # Calcular el factor de escala para normalizar las coordenadas
    escala_x = resolucion_actual[0] / resolucion_referencia[0]
    escala_y = resolucion_actual[1] / resolucion_referencia[1]

    # Calcular las coordenadas normalizadas y retornar
    return int(posicion_referencia[0] * escala_x), int(posicion_referencia[1] * escala_y)
