import datetime
import os
import rpa as r
import pyautogui as p
import pandas as pd


def hora():
    return datetime.datetime.now().strftime('%H%M%S')


def log(mensaje, imprimir=True):
    fecha = datetime.datetime.now().strftime('%Y%m%d')
    if not os.path.exists(f'log{fecha}.log'):
        with open(f'log{fecha}.log', 'w') as f:
            f.write('fecha\n')
    with open(f'log{fecha}.log', 'a') as f:
        f.write(f'{hora()}: {mensaje} \n')
        if imprimir:
            print(f'{hora()}: {mensaje}')


fecha_hora = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

r.init(turbo_mode=True)
archivo_descarga = f'active_loans_input_{fecha_hora}.xlsx'
log(f'Descargando archivo {archivo_descarga}')
r.download('https://botsdna.com/ActiveLoans/input.xlsx', archivo_descarga)
r.wait()
log(f'Verificando descarga de archivo {archivo_descarga}')
if os.path.exists(archivo_descarga):
    log(f'Archivo {archivo_descarga} descargado correctamente')
else:
    log(f'No se encontró el archivo {archivo_descarga}')
p.hotkey('alt', 'f4')
log('Proceso finalizado')
exit()
r.url('https://botsdna.com/ActiveLoans/')
r.wait()
df = pd.read_excel('active_loans_input.xlsx')



for index, row in df.iterrows():
    r.type('//input[@ng-reflect-name="labelFirstName"]', row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]', row['Last Name'])
    r.type('//input[@ng-reflect-name="labelCompanyName"]', row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]', row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]', row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]', row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]', str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

r.snap('/html/body/app-root/div[2]', 'teleorg_rpa/screenshot.png')
r.close()

print('Proceso finalizado!')



