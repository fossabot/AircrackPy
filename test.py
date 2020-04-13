#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Pequeño ejemplo de lo que puede hacer.


from aircrack import AircrackPy
cmd=AircrackPy()
from sys import exit
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
    print("""
1) Diccionario
2) Crunch""")
    x=input()
    while True:
        if x=="1":
            print("Ingresa tu diccionario")
            dic=input("")
            print("Nombre del HandShake:")
            pcap=input("")
            break
        elif x=="2":
            dic=""
            print("""Numeros de 10 digitos""")
            x=input("Prefijo:")
            print("Nombre del HandShake, debe de terminar en _<MAC>.cap, cada par separado por '-' o ':'")
            pcap=input("")
            break
        else:
            print("Escoge bien")
            
    print("Primero un test de velocidad, espera por favor...")
    print(cmd.test())

    print("Listo, comencemos")
    cmd.wpa(dic,pcap,x)
    exit()

except Exception as e:
    print("UPSS ocurrio un error\n"+str(e))
    exit()
    
