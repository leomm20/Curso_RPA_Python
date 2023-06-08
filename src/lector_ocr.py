import os
import pytesseract as p

"""
necesario instalar https://github.com/UB-Mannheim/tesseract/wiki  (lenguajes: english y spanish)
"""

p.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # needed for Windows as OS

ruta_archivo = os.getcwd() + r'\windows\Descargas.png'
texto_obtenido = p.image_to_string(ruta_archivo)
print(texto_obtenido)
print('\n' + '*' * 100 + '\n')

ruta_archivo = os.getcwd() + r'\screenshots\ejemplo1.png'
texto_obtenido = p.image_to_string(ruta_archivo)
print(texto_obtenido)
