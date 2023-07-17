import datetime
import rpa as r
import pandas as pd

df = pd.read_excel('challenge.xlsx')
r.init()  # r.init(turbo_mode=True)
r.url('https://rpachallenge.com/')
r.wait()
r.click('//button[text()="Start"]')

for index, row in df.iterrows():
    r.type('//input[@ng-reflect-name="labelFirstName"]', row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]', row['Last Name'])
    r.type('//input[@ng-reflect-name="labelCompanyName"]', row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]', row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]', row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]', row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]', str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

fecha_hora = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
r.snap('/html/body/app-root/div[2]', f'screenshot{fecha_hora}.png')
r.close()
print('Proceso finalizado!')
