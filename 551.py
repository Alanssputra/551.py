import requests
import json
import sys
import os
import time
from requests import session
import datetime
from random import SystemRandom
import random
from datetime import datetime

P = '\033[95m'
CYAN = '\033[96m'
DARK = '\033[36m'
B = '\033[94m'
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
BO = '\033[1m'
UNDER = '\033[4m'
N = '\033[0m'

def auto_besarikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['5','6','7','8','9']
			h = random.SystemRandom()
			i = h.choice(g)
			print(f"{G}✹ Next Periode{R}[{Y}{f}{R}] {G}•|• {DARK}Prediksi{R}({Y}{UNDER}BESAR{N}{BO}{R}) {G}•|• {Y}Angka : {i}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarikut()
			
			
			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['0','1','2','3','4']
			h = random.SystemRandom()
			i = h.choice(g)
			print(f"{G}✹ Next Periode{R}[{Y}{f}{R}] {G}•|• {DARK}Prediksi{R}({Y}{UNDER}KECIL{N}{BO}{R}) {G}•|• {Y}Angka : {i}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecilikut()
			
			
def countdownTimer ():
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{Y}{BO}{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
			
def gameissue ():
			
			data = {
			'typeid' : '1',
			'language' : '1'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetGameIssue', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('IssueNumber')
			with open('issuenumber.txt', 'w') as f:
				f.write(str(d))
				f.close()
				
def taruhanbesarikut ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f"{DARK}HASIL : {G}[{e}] WINNNNNER BESAR {f}✅🥰")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			 rumusikut()
			elif f < '5':
			 print(f"{DARK}HASIL : {R}[{e}] MINNNNNER KECIL {f}⛔😭")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			 rumuslawan()
			
			
def taruhankecilikut ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f"{DARK}HASIL : {R}[{e}] MINNNNNER BESAR {f}⛔😭")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			 rumuslawan()
			elif f < '5':
			 print(f"{DARK}HASIL : {G}[{e}] WINNNNNER KECIL {f}✅🥰")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumusikut()
def halaman1 ():
      data = {
      'typeid' : '1',
      'pageno' : '1',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman1.txt", 'w') as f:
       f.write(str(e1))
       f.close()
			
def rumusikut ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(j)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result.txt").read()
      if res == '0':
       auto_kecilikut()
      elif res == '1':
       auto_kecilikut()
      elif res == '2':
       auto_kecilikut()
      elif res == '3':
       auto_kecilikut()
      elif res == '4':
       auto_kecilikut()
      elif res == '5':
       auto_besarikut()
      elif res == '6':
       auto_besarikut()
      elif res == '7':
       auto_besarikut()
      elif res == '8':
       auto_besarikut()
      elif res == '9':
       auto_besarikut()
      elif res == '10':
       auto_kecilikut()
      elif res == '11':
       auto_kecilikut()
      elif res == '12':
       auto_kecilikut()
      elif res == '13':
       auto_kecilikut()
      elif res == '14':
       auto_kecilikut()
      elif res == '15':
       auto_besarikut()
      elif res == '16':
       auto_besarikut()
      elif res == '17':
       auto_besarikut()
      elif res == '18':
       auto_besarikut()
      elif res == '19':
       auto_besarikut()
      elif res == '20':
       auto_kecilikut()
      elif res == '21':
       auto_kecilikut()
      elif res == '22':
       auto_kecilikut()
      elif res == '23':
       auto_kecilikut()
      elif res == '24':
       auto_kecilikut()
      elif res == '25':
       auto_besarikut()
      elif res == '26':
       auto_besarikut()
      else:
       auto_kecilikut()
       
def auto_besarlawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['5','6','7','8','9']
			h = random.SystemRandom()
			i = h.choice(g)
			print(f"{G}✹ Next Periode{R}[{Y}{f}{R}] {G}•|• {DARK}Prediksi{R}({Y}{UNDER}BESAR{N}{BO}{R}) {G}•|• {Y}Angka : {i}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarlawan()
			
			
			
def auto_kecillawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['0','1','2','3','4']
			h = random.SystemRandom()
			i = h.choice(g)
			print(f"{G}✹ Next Periode{R}[{Y}{f}{R}] {G}•|• {DARK}Prediksi{R}({Y}{UNDER}KECIL{N}{BO}{R}) {G}•|• {Y}Angka : {i}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecillawan()
				
def taruhanbesarlawan ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f"{DARK}HASIL : {G}[{e}] WINNNNNER BESAR {f}✅🥰")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			 rumuslawan()
			elif f < '5':
			 print(f"{DARK}HASIL : {R}[{e}] MINNNNNER KECIL {f}⛔😭")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			 rumusikut()
			
			
def taruhankecillawan ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f"{DARK}HASIL : {R}[{e}] MINNNNNER BESAR {f}⛔😭")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			 rumusikut()
			elif f < '5':
			 print(f"{DARK}HASIL : {G}[{e}] WINNNNNER KECIL {f}✅🥰")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumuslawan()
			
def rumuslawan ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '9',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(j)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("result.txt").read()
      if res == '0':
       auto_besarlawan()
      elif res == '1':
       auto_besarlawan()
      elif res == '2':
       auto_besarlawan()
      elif res == '3':
       auto_besarlawan()
      elif res == '4':
       auto_besarlawan()
      elif res == '5':
       auto_kecillawan()
      elif res == '6':
       auto_kecillawan()
      elif res == '7':
       auto_kecillawan()
      elif res == '8':
       auto_kecillawan()
      elif res == '9':
       auto_kecillawan()
      elif res == '10':
       auto_besarlawan()
      elif res == '11':
       auto_besarlawan()
      elif res == '12':
       auto_besarlawan()
      elif res == '13':
       auto_besarlawan()
      elif res == '14':
       auto_besarlawan()
      elif res == '15':
       auto_kecillawan()
      elif res == '16':
       auto_kecillawan()
      elif res == '17':
       auto_kecillawan()
      elif res == '18':
       auto_kecillawan()
      elif res == '19':
       auto_kecillawan()
      elif res == '20':
       auto_besarlawan()
      elif res == '21':
       auto_besarlawan()
      elif res == '22':
       auto_besarlawan()
      elif res == '23':
       auto_besarlawan()
      elif res == '24':
       auto_besarlawan()
      elif res == '25':
       auto_kecillawan()
      elif res == '26':
       auto_kecillawan()
      else:
       auto_besarikut()
 


b = datetime.now()
c = b.day
f = b.hour
d = 5
e = 6
f = 7
g = 8
h = 1
if c == b:
	os.system("clear")
	os.system("rm 55fivev2.py")
	time.sleep
	exit(10)
else:
	os.system("clear")
	print(R+"▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▒█░▄▀ ▒█▀▀▀█ ▀█▀\n▒█▄▄█ ▒█▄▄▀ ▒█▀▀▀ ▒█░▒█ ▒█░ ▒█▀▄░ ░▀▀▀▄▄ ▒█░\n▒█░░░ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▀ ▄█▄ ▒█░▒█ ▒█▄▄▄█ ▄█▄ \n\n█▀▀ █▀▀ 　 ▒█▀▀▀ ▀█▀ ▒█░░▒█ ▒█▀▀▀\n▀▀▄ ▀▀▄ 　 ▒█▀▀▀ ▒█░ ░▒█▒█░ ▒█▀▀▀\n▄▄▀ ▄▄▀ 　 ▒█░░░ ▄█▄ ░░▀▄▀░ ▒█▄▄▄")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	halaman1()
	aa = open("halaman1.txt").read()
	if aa > '4':
	 rumusikut()
	elif aa < '5':
	 rumuslawan()
	else:
	 rumuslawan()