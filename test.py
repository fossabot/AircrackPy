#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Pequeño ejemplo de lo que puede hacer.


from aircrack import AircrackPy
cmd=AircrackPy()
from time import sleep
"""
##################################
# CODED BY 4nth0nySLT            #
# github.com/4nth0nySLT          #
# t.me/Anth0nySLT                #
#            ECUADOR             #
##################################
"""
try:
    print("Ingresa tu diccionario:")
    dic=input("")
    print("Nombre del HandShake:")
    pcap=input("")
    print("Primero un test de velocidad, espera por favor...")
    print(cmd.test())
    sleep(3)
    print("Listo, comencemos")
    cmd.wpa(dic,pcap)
    exit()

except Exception as e:
    print("UPSS ocurrio un error\n"+e)
    exit()
    
