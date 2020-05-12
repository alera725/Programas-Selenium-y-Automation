#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:01:00 2020

@author: Aera
"""

# Tarea 2 Concesionaria de autos

Datos = list()
Nombre = {}
Apellido = {}
Marca = {}
Puertas = {}
Color = {}
Precio_total = {}

# dictionary of brand prices 
Marca_precio = {'Ford':100000,'Chevrolet':120000,'Fiat':80000}
    
# dictionary of color prices 
Color_precio = {'Blanco':100000,'Azul':20000,'Negro':30000}
    
# dictionary of door´s prices 
Puertas_precio = {2:50000,4:65000,5:30000}

# Input Num cientes
num_clientes = input('Escribir el numero de clientes que desea capturar: ')
b=0
while b==0:
        try:
            num_clientes = int(num_clientes)
            b=1
        except ValueError:
            print ("Por favor capture esta variable numérica")
            num_clientes = input('Escribir el numero de clientes que desea capturar: ')

# For cycle 
for i in range(1,num_clientes+1):
    
    # Nombre input 
    print("Ingresar los datos del ciente No.", i)
    
    Nombre[i] = input('Escribir el Nombre: ')
    while len(Nombre[i].strip()) == 0:
        print('Por favor capture esta variable de la manera solicitada')
        Nombre[i] = input('Escribir el Nombre: ')
    
    # Apellido input 
    Apellido[i] = input('Escribir el Apellido: ')
    while len(Apellido[i].strip()) == 0:
        print('Por favor capture esta variable de la manera solicitada')
        Apellido[i] = input('Escribir el Apellido: ')
    
    # Marca input 
    Marca[i] = input('Selecciona la marca (Ford, Chevrolet o Fiat): ')
    while len(Marca[i].strip()) == 0:
        print('Por favor capture esta variable de string')
        Marca[i] = input('Selecciona la marca (Ford, Chevrolet o Fiat): ')
    if (Marca[i]=='ford'):
        Marca[i]='Ford'
    elif(Marca[i]=='chevrolet'):
        Marca[i]='Chevrolet'
    else:
        Marca[i]='Fiat'
    
    # Puertas input 
    Puertas[i] = input('Selecciona el número de puertas (2, 4 o 5): ')
    x=0
    while x==0:
        try:
            Puertas[i] = int(Puertas[i])
            x=1
        except ValueError:
            print ("Por favor capture esta variable numérica")
            Puertas[i] = input('Selecciona el número de puertas (2, 4 o 5): ')
    if(Puertas[i] != 2 and Puertas[i] != 4 and Puertas[i] != 5):
        Puertas[i] = 2
    else:
        Puertas[i] = Puertas[i]
    
    # Color input 
    Color[i] = input('Selecciona el color (Blanco, Azul o Negro): ')
    while len(Color[i].strip()) == 0:
        print('Por favor capture esta variable de la manera solicitada')
        Color[i] = input('Selecciona el color (Blanco, Azul o Negro): ')
    if (Color[i]=='blanco'):
        Color[i]='Blanco'
    elif(Color[i]=='azul'):
        Color[i]='Azul'
    else:
        Color[i]='Negro'
    
    # Datos de compra y el precio total
    Precio_total[i]= Marca_precio[Marca[i]] + Puertas_precio[Puertas[i]] + Color_precio[Color[i]]

# Print Data
for i in range(1,num_clientes+1):
    print("\n""Datos de compra No.",i,"\n","\n",'Nombre:', Nombre[i], "\n", 'Apellido:', Apellido[i], "\n", 'Marca:', Marca[i], '\n','No. Puertas:', Puertas[i], '\n','Color:', Color[i], '\n','Precio: $', Precio_total[i]) 





