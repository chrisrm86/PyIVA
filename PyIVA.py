#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       PyIVA
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
from tkinter import *
from tkinter.messagebox import askokcancel
from tkinter.messagebox import showinfo
from sys import exit
from tkinter import font
from tkinter import PhotoImage

class PyIVA():
	def __init__(self, parent=None, **configs):
		self.frame = parent
		self.frame.geometry('400x260')
		self.frame.resizable(False, False)
		self.frame.title('PyIVA')
		self.frame.iconbitmap('media/icono1.ico')

		self.principalContainer = Frame(self.frame, bg='beige')
		self.principalContainer.pack(expand=YES, fill=BOTH)

		self.c1 = Frame(self.principalContainer, bg='beige', width=100, height=100)
		self.c1.pack(expand=NO, fill=Y, side=LEFT)
		self.c2 = Frame(self.principalContainer, bg='beige', width=240, height=100)
		self.c2.pack(expand=NO, fill=Y, side=RIGHT)

		self.btn1 = Button(self.c1, text='Calcular 0.21%', command=self.calcular_21, height=2, width=20)
		self.btn1.pack(padx=10, pady=12)
		self.btn2 = Button(self.c1, text='Calculo personalizado', command=self.calculo_personalizado, height=2, width=20)
		self.btn2.pack(padx=10, pady=12)
		self.btn3 = Button(self.c1, text='Acerca de', command=self.info, height=2, width=20)
		self.btn3.pack(padx=10, pady=12)
		self.btn4 = Button(self.c1, text='Salir', command=self.salir, height=2, width=20)
		self.btn4.pack(padx=10, pady=12)

		self.etiq1 = Label(self.c2, text='Valor de producto:', bg='Beige', fg='black')
		self.etiq1.pack(padx=10, pady=10)

		entrada=StringVar()
		self.tipografia = font.Font(family="Helvetica", size=10, weight="bold")

		ruta = "media/"
		photo1 = PhotoImage(file=ruta + "imagen2.gif")
		label1 = Label(self.c2, image=photo1)
		label1.image=photo1
		label1.pack(side=BOTTOM, pady=10, padx=5)

		self.entrada_datos = Entry(self.c2, width=50, textvariable=entrada)
		self.entrada_datos.pack(padx=20, pady=5)

		self.etiq2 = Label(self.c2, text='', bg='beige', fg='black')
		self.etiq2.pack(padx=20, pady=10)

	def calcular(self):
		precio_producto = str(self.entrada_datos.get())
		vacio = ''
		if precio_producto == vacio:
			self.ventana_error1()
		else:
			precio_producto = int(self.entrada_datos.get())

	def calcular_21(self):
		try:
			precio_producto = float(self.entrada_datos.get())
			iva21 = 0.21
			if precio_producto < 0:
				self.ventana_error2()
			else:
				precio_con_iva = precio_producto * iva21
				precio_final = precio_con_iva + precio_producto
				self.etiq2.config(text='El precio final es: '+ '$' + str(precio_final), font=self.tipografia)
		except ValueError:
			self.ventana_error1()

	def calculo_personalizado(self):
		entrada_valor_personalizado=StringVar()
		entrada_iva_personalizado=StringVar()
		self.cPersonalizado = Toplevel()
		self.cPersonalizado.geometry('300x150')
		self.cPersonalizado.title('Calculo personalizado')
		self.cPersonalizado.resizable(False,False)

		self.etiq3 = Label(self.cPersonalizado, text='Valor producto:')
		self.etiq3.pack()
		self.entrada_valor_personalizado = Entry(self.cPersonalizado, width=30, textvariable=entrada_valor_personalizado)
		self.entrada_valor_personalizado.pack()
		self.etiq4 = Label(self.cPersonalizado, text='IVA porcentaje')
		self.etiq4.pack()
		self.entrada_valor_iva = Entry(self.cPersonalizado, width=30, textvariable=entrada_iva_personalizado)
		self.entrada_valor_iva.pack()

		self.btn5 = Button(self.cPersonalizado, text='Calcular', command=self.calcular_personalizado)
		self.btn5.pack(pady=10)
		self.etiq5 = Label(self.cPersonalizado, text='')
		self.etiq5.pack(side=BOTTOM, pady=2)
	
	def calcular_personalizado(self):
		try:
			valor_pers = float(self.entrada_valor_personalizado.get())
			valor_iva = float(self.entrada_valor_iva.get())
			if valor_pers <0:
				self.mensaje_error2()
			elif valor_iva <0:
				self.mensaje_error2()
			else:
				precio_con_iva_personalizado = valor_pers * valor_iva
				precio_pers_final = precio_con_iva_personalizado + valor_pers
				self.etiq5.config(text='El precio final es: '+'$'+str(precio_pers_final), font=self.tipografia)
		except ValueError:
			self.mensaje_error1()

	def ventana_error1(self):
		showinfo(title='PyIVA', message='Ingrese un valor numérico.')

	def ventana_error2(self):
		showinfo(title='PyIVA', message='Ha ingresado un número negativo, operación no válida.')

	def mensaje_error1(self):
		self.etiq5.config(text='Error - Datos incorrectos o incompletos.', fg='red')

	def mensaje_error2(self):
		self.etiq5.config(text='Error - Ha ingresado números negativos.', fg='red')

	def info(self):
		showinfo(title='Acerca de', message="""PyIVA v1.0 - Desarrollado por Christian Morán.\ne-mail: christianrmoran86@gmail.com \nMore code in https://github.com/chrisrm86
		""")

	def salir(self):
		consulta = askokcancel('PyIVA', "¿Desea salir de la aplicación?")
		if consulta:
			exit()

if __name__=='__main__':
	root = Tk()
	PyIVA(root)
	root.mainloop()