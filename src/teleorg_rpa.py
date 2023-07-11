import rpa as r
import pandas as pd

df = pd.read_excel('teleorg_rpa/challenge.xlsx')

r.init(turbo_mode=True)
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

r.snap('/html/body/app-root/div[2]', 'teleorg_rpa/screenshot.png')
r.close()

print('Proceso finalizado!')



