from datetime import datetime
import time
import dateutil
poezda = [
{
'N_poezda':221,
'Punkt_pr':'Minsk',
't_pr':'15:00:00',
'Punkt_otpr':'Brest',
't_otpr':'10:20:00'
},
{
'N_poezda':342,
'Punkt_pr':'Minsk',
't_pr':'17:35:00',
'Punkt_otpr':'Gomel',
't_otpr':'12:22:00'
},
{
'N_poezda':518,
'Punkt_pr':'Kaliningrad',
't_pr':'20:39:00',
'Punkt_otpr':'Minsk',
't_otpr':'12:12:00'
},
{
'N_poezda':222,
'Punkt_pr':'Vitebsk',
't_pr':'06:12:00',
'Punkt_otpr':'Moskva',
't_otpr':'20:00:00'
},
{
'N_poezda':290,
'Punkt_pr':'Gdansk',
't_pr':'08:12:30',
'Punkt_otpr':'Grodno',
't_otpr':'22:00:12'
},
]

for i in poezda:
    if datetime.strptime(i['t_otpr'],'%H:%M:%S') + relativedelta(hours = 7,minutes = 20) > datetime.strptime(i['t_pr'],'%H:%M:%S'):
        print ('OK')