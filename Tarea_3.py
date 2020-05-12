#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:32:04 2020

@author: Aera
"""
# Tarea 3 Concesionaria de autos

# Inicailizar variables a utilizar
Datos = list()
Nombre = {}
Apellido = {}
Marca = {}
Puertas = {}
Color = {}
Precio_total = {}

aut_chevy = ['chevrolet','Chevrolet','CHEVROLET']
aut_ford = ['ford','Ford','FORD']
aut_fiat = ['fiat','FIAT','Fiat']
aut = aut_chevy+aut_ford+aut_fiat
puert =[2,4,5]
colo_blanco = ['Blanco','blanco','BLANCO']
colo_negro = ['Negro','negro','NEGRO']
colo_azul = ['Azul','azul','AZUL']
colo = colo_blanco+colo_negro+colo_azul

# dictionary of brand prices 
Marca_precio = {'Ford':100000,'Chevrolet':120000,'Fiat':80000}
    
# dictionary of color prices 
Color_precio = {'Blanco':100000,'Azul':20000,'Negro':30000}
    
# dictionary of door´s prices 
Puertas_precio = {2:50000,4:65000,5:30000}

#Inicializar parametros 
i = 0
otro = 'Si'

# While 
while otro == 'Si' or otro=='si' or otro == 'SI':
    
    i = i+1
    
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
    while len(Marca[i].strip()) == 0 or Marca[i] not in aut:
        print('Por favor capture esta variable tipo string eligiendo una de las marcas mencionadas')
        
        Marca[i] = input('Selecciona la marca (Ford, Chevrolet o Fiat): ')
    if (Marca[i] in aut_ford):
        Marca[i]='Ford'
    elif(Marca[i] in aut_chevy):
        Marca[i]='Chevrolet'
    else:
        Marca[i]='Fiat'

    
    # Puertas input 
    Puertas[i] = input('Selecciona el número de puertas (2, 4 o 5): ')
    x = 0
    while (x == 0):
        try:
            Puertas[i] = int(Puertas[i])
            if(Puertas[i] not in puert):
                while(Puertas[i] not in puert):
                    print ("Por favor capture esta variable numérica de la manera solicitada")
                    Puertas[i] = int(input('Selecciona el número de puertas (2, 4 o 5): '))
                x=1
            else:
                x=1
        except ValueError:
            print ("Por favor capture esta variable numérica de la manera solicitada")
            Puertas[i] = input('Selecciona el número de puertas (2, 4 o 5): ')
    
    
    # Color input 
    Color[i] = input('Selecciona el color (Blanco, Azul o Negro): ')
    while len(Color[i].strip()) == 0 or Color[i] not in colo:
        print('Por favor capture esta variable de la manera solicitada')
        Color[i] = input('Selecciona el color (Blanco, Azul o Negro): ')
    if (Color[i] in colo_blanco):
        Color[i]='Blanco'
    elif(Color[i] in colo_azul):
        Color[i]='Azul'
    else:
        Color[i]='Negro'
    
    # Datos de compra y el precio total
    Precio_total[i]= Marca_precio[Marca[i]] + Puertas_precio[Puertas[i]] + Color_precio[Color[i]]
    
    otro = input('¿Desea capturar otro cliente? (Escriba Si o No): ')
    while (len(otro.strip()) == 0 or otro not in ['Si','si','no','No','SI','NO']):
        print('Por favor capture esta variable de la manera solicitada')
        otro = input('¿Desea capturar otro cliente? (Escriba Si o No): ')
        

# Aplicar descuento si este existe
if (i>5):
    desc = .10
    if(i>10):
        desc = .15
        if(i>50):
            desc = .18
else:
    desc = 0
    

# Print Data
j=i
for i in range(1,j+1):
    print("\n""Datos de compra No.",i,"\n","\n",'Nombre:', Nombre[i], "\n", 'Apellido:', Apellido[i], "\n", 'Marca:', Marca[i], '\n','No. Puertas:', Puertas[i], '\n','Color:', Color[i], '\n','Precio: $', Precio_total[i]*(1-desc)) 