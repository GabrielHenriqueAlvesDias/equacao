import emoji
from time import sleep 
import os
import math
def linp(): 
    if os.name == 'nt':
	    os.system('cls')
    else:
    	os.system('clear')
   	
def grau():
	print("calculo de Basekara \n")
	a = int(input('Qual é valor de A: '))
	b = int(input('Qual é valor de B: '))
	c = int(input('Qual é valor de C: '))
	delta=b**2-4*a*c
	linp()
	if delta ==0:
		x1=(-b + math.sqrt(delta)) / (2*a)
		print('A unica raiz e:',x1)
	else:
		if delta <=-1:
			print('nao tem raiz')
		else:
			x1=(-b + math.sqrt(delta)) / (2*a)
			x2=(-b-math.sqrt(delta)) / (2*a)
			print('                              Δ=b²-4.a.c')
			print('                                 2.a\n')
			print(f'                   Δ={b}²-4.{a}.{c}')
			print(emoji.emojize(f'   	                             2.{a}\n:thumbs_up:'))
			print(x1,x2)
      	

grau()