import pyautogui as pg
import webbrowser as web 
import time
import pandas as pd
import datetime


data=pd.read_csv('leads1.csv')
data_dict=data.to_dict('list')
leads=data_dict['LeadNumber']
messages=data_dict['Message']
combo=[]
for i in range(0,len(leads)):
    nls=[]
    nls.append(leads[i])
    nls.append(messages[i])
    combo.append(nls)
first=True

tim=""
#enter the time in 24 hour format
ls1=['8:0','17:35','12:0','20:0','23:0','23:30','0:0','0:30']
#for i in range(0,60):
  #tim=tim+"16:"+str(i*2)
  #ls1.append(tim)
  #tim=""
#time_slots=ls1
time_slots=ls1
while True:
	mytime=datetime.datetime.now()
	current_time=str(mytime.hour)+':'+str(mytime.minute)
	if current_time in time_slots:
		for values in combo:
			web.open("https://web.whatsapp.com/send?phone="+values[0]+"&text="+values[1])
			if first:
				time.sleep(8)
				first=False
			width,height=pg.size()
			pg.click(width/2,height/2)
			time.sleep(10)
			pg.press('enter')
			time.sleep(10)
			pg.hotkey('ctrl','w')
		time_slots.remove(current_time)
	else:
		pass
		#print("waiting...")