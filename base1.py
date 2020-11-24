# -*- coding: utf-8 -*-

import math

#Valeurs

b_start = ''
b_end = ''
valeur = ''
result = ''

#Conversion

def base2_to_base10(n):
	result = ''
	return("La conversion de la base {} dans la base {} de la représentation {} est : {}.").format(b_start,b_end,valeur,result)

def base2_to_base16(n):
	result = ''
	return("La conversion de la base {} dans la base {} de la représentation {} est : {}.").format(b_start,b_end,valeur,result)

def base10_to_base2(n):
	result = ''
	return("La conversion de la base {} dans la base {} de la représentation {} est : {}.").format(b_start,b_end,valeur,result)

def base10_to_base16(n):
	result = ''
	return("La conversion de la base {} dans la base {} de la représentation {} est : {}.").format(b_start,b_end,valeur,result)

def base16_to_base2(n):
	result = ''
	return("La conversion de la base {} dans la base {} de la représentation {} est : {}.").format(b_start,b_end,valeur,result)

def base16_to_base10(n): 
	result = ''
	return("La conversion de la base {} dans la base {} de la représentation {} est : {}.").format(b_start,b_end,valeur,result)


#Demande utilisateur

#Demande de la base de départ

def base_départ():
	print("Base 2 = (A) , Base 10 = (B) , Basse 16 = (C)")
	return input("Donnez la base de départ : ")

 
b_start = base_départ()
while b_start not in ('A', 'B', 'C'):
	print("Erreur, mauvaise entrée")
	b_start = base_départ()
 
print(b_start)

#Demande de la base de fin

def base_fin():
	print("Base 2 = (A) , Base 10 = (B) , Base 16 = (C)")
	return input("Donnez la base de fin : ")
 
b_end = base_fin()
while b_end not in ('A', 'B', 'C'):
	print("Erreur, mauvaise entrée")
	b_end = base_fin()
 
print(b_end)

#Demande de la valeur à convertir

while True:
	try:
		valeur = int(input("Donnez la valeur à convertir : "))
		break
	except:
		print("La valeur n'est pas un entier")
print(valeur)

#Choix de la base

if b_start == 'A' and b_end == 'B' :
	print(base2_to_base10(valeur))
elif b_start == 'A' and b_end == 'C' :
	print(base2_to_base16(valeur))
elif b_start == 'B' and b_end == 'A' :
	print(base10_to_base2(valeur))
elif b_start == 'B' and b_end == 'C' :
	print(base10_to_base16(valeur))
elif b_start == 'C' and b_end == 'A' :
	print(base16_to_base2(valeur))
elif b_start == 'C' and b_end == 'B' :
	print(base16_to_base10(valeur))
else:
	print('La base de départ et de fin et la même.')
