from pywinauto import application
import os, time

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:heradenk /pwd:tjd4389! /pwdcert:tjd438989! /autostart')
time.sleep(60)