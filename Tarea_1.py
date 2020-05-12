#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:11:28 2020

@author: Aera
"""

# Convertir la variable en un nombre 
Nombre = input('Escribir el nombre del Alumno: ')
while len(Nombre.strip()) == 0:
    print('No puede dejar en blanco esta variable')
    Nombre = input('Escribir el nombre del Alumno: ')

Apellido = input('Escribir el apellido del Alumno: ')
while len(Apellido.strip()) == 0:
    print('No puede dejar en blanco esta variable')
    Apellido = input('Escribir el apellido del Alumno: ')


Matematicas = input('Escribir la calificacion de Matematicas (de forma numérica): ')
x=0
while x==0:
    try:
        Matematicas = int(Matematicas)
        x=1
    except ValueError:
        print ("No puede dejar en blanco esta variable numérica")
        Matematicas = input('Escribir la calificacion de Matematicas (de forma numérica): ')
        
        
Literatura = input('Escribir la calificacion de Literatura (de forma numérica): ')
x=0
while x==0:
    try:
        Literatura = int(Literatura)
        x=1
    except ValueError:
        print ("No puede dejar en blanco esta variable numérica")
        Literatura = input('Escribir la calificacion de Literatura (de forma numérica): ')


Fisica = input('Escribir la calificacion de Fisica (de forma numérica): ')
x=0
while x==0:
    try:
        Fisica = int(Fisica)
        x=1
    except ValueError:
        print ("No puede dejar en blanco esta variable numérica")
        Fisica = input('Escribir la calificacion de Fisica (de forma numérica): ')



calificaciones = Matematicas,Literatura,Fisica

def promedio(n):
    return sum(n)/len(n)

promedio = promedio(calificaciones)

if (promedio >= 9):
    estatus = 'Alumno destacado'
elif (promedio >= 6 ):
    estatus = 'Aprobado'
elif (promedio > 4 and promedio <6 ):
    estatus = 'A recuperatorio'
else:
    estatus = 'Insuficiente'

Imprimir_nombre = input('Desea imprimir el nombre el alumno (a=si, b=no):  ')
Imprimir_apellido = input('Desea imprimir el apellido el alumno (a=si, b=no): ')
Imprimir_promedio = input('Desea imprimir el promedio el alumno (a=si, b=no): ')

if (Imprimir_nombre == 'a' and Imprimir_apellido == 'a' and Imprimir_promedio == 'a'):
    print("\n",'Nombre: ', Nombre, "\n", 'Apellido: ', Apellido, "\n", 'Promedio: ', promedio, '\n','Estatus: ', estatus) 
elif (Imprimir_nombre == 'b' and Imprimir_apellido == 'a' and Imprimir_promedio == 'a'):
    print("\n",'Apellido: ', Apellido, "\n", 'Promedio: ', promedio, '\n','Estatus: ', estatus)
elif (Imprimir_nombre == 'b' and Imprimir_apellido == 'b' and Imprimir_promedio == 'a'):
    print("\n",'Promedio: ', promedio, '\n','Estatus: ', estatus)
elif (Imprimir_nombre == 'b' and Imprimir_apellido == 'a' and Imprimir_promedio == 'b'):
    print("\n",'Apellido: ', Apellido)
elif (Imprimir_nombre == 'a' and Imprimir_apellido == 'b' and Imprimir_promedio == 'b'):
    print("\n",'Nombre: ', Nombre)
elif (Imprimir_nombre == 'a' and Imprimir_apellido == 'a' and Imprimir_promedio == 'b'):
    print("\n",'Nombre: ', Nombre, 'Apellido: ', Apellido)







