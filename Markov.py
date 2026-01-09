import numpy as np
from numpy.linalg import matrix_power
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

class Ventana:
	def __init__(self):
		self.mostrar_mensaje()
		self.Ventana = Tk()
		self.Ventana.geometry('1000x600')
		self.Ventana.title('Investigación de Operaciones')
		self.Ventana.config(bg='bisque2')

		self.canvas = Canvas(self.Ventana, bg='bisque2')
		self.canvas.grid(row=0, column=0, sticky="nsew")

		Ventana_Marco0 = Frame(self.canvas, bg="bisque2")
		Ventana_Marco0.config(padx='10', pady='10', borderwidth=1, relief='ridge')
		self.canvas.create_window((0, 0), window=Ventana_Marco0, anchor="nw")

		Ventana_Marco1 = Frame(Ventana_Marco0, bg="bisque2")
		Ventana_Marco1.config(padx='10', pady='10', borderwidth=1, relief='ridge')

		self.scrollbar = ttk.Scrollbar(self.Ventana, orient="vertical", command=self.canvas.yview)
		self.scrollbar.grid(row=0, column=1, sticky="ns")

		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

		self.Ventana.grid_rowconfigure(0, weight=1)
		self.Ventana.grid_columnconfigure(0, weight=1)
		self.Ventana.grid_columnconfigure(1, weight=0)

		Ventana_Marco = Frame(Ventana_Marco0, bg="bisque2")
		Ventana_Marco.grid(row=1, column=2, padx=10, pady=20)
		self.Ventana_Marco1 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco1.grid(row=2, column=2, padx=10, pady=20)
		self.Ventana_Marco2 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco2.grid(row=2, column=3, padx=1, pady=20)
		self.Ventana_Marco3 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco3.grid(row=3, column=2, padx=10, pady=20)
		self.Ventana_Marco4 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco4.grid(row=4, column=2, padx=10, pady=20)
		self.Ventana_Marco5 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco5.grid(row=5, column=2, padx=10, pady=20)
		self.Ventana_Marco6 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco6.grid(row=5, column=3, padx=1, pady=20)
		self.Ventana_Marco7 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco7.grid(row=6, column=2, padx=10, pady=20)
		self.Ventana_Marco8 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco8.grid(row=7, column=2, padx=1, pady=20)
		self.Ventana_Marco9 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco9.grid(row=8, column=2, padx=10, pady=20)
		self.Ventana_Marco10 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco10.grid(row=9, column=2, padx=10, pady=20)
		self.Ventana_Marco11 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco11.grid(row=10, column=2, padx=10, pady=20)
		self.Ventana_Marco12 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco12.grid(row=11, column=2, padx=10, pady=20)
		self.Ventana_Marco13 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco13.grid(row=12, column=2, padx=10, pady=20)
		self.Ventana_Marco14 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco14.grid(row=13, column=2, padx=10, pady=20)
		self.Ventana_Marco15 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco15.grid(row=14, column=2, padx=10, pady=20)
		self.Ventana_Marco16 = Frame(Ventana_Marco0, bg="bisque2")
		self.Ventana_Marco16.grid(row=15, column=2, padx=10, pady=20)

		Ventana_EtiqEsta = Label(Ventana_Marco, text='Cuantos estados son:', font=('Calibri', 12), bg='bisque2')
		Ventana_EtiqEsta.grid(row=1, column=0)
		Ventana_ValorF = StringVar()
		Ventana_EntradaFIL = Entry(Ventana_Marco, textvar=Ventana_ValorF, width='10', font=('Calibri', 12))
		Ventana_EntradaFIL.grid(row=1, column=1, padx=20)

		Ventana_BotonCrear = Button(Ventana_Marco, text = 'Crear matriz', command = lambda:self.Crear_Matriz(Ventana_EntradaFIL))
		Ventana_BotonCrear.grid(row = 1, column = 3, padx = 20)

		self.Ventana.mainloop()

	def mostrar_mensaje(self):
			messagebox.showinfo("Mensaje", "Para ver la información agregada recientemente, mueve la ventana para actualizar la barra de desplazamiento.")

	def Crear_Matriz(self, Filas):

		tama_strFil = Filas.get()
		try:
			self.tama1 = int(tama_strFil)
			if self.tama1 == 1:
				messagebox.showerror("Error", "El tamaño de la matriz debe no debe ser 1.")
				return
		except:
			messagebox.showerror("Error", "El tamaño de la matriz debe ser un número entero.")
			return

		Matriz = []
		for fil in range(self.tama1):
			fila= []
			for col in range(self.tama1):
				Dato = Entry(self.Ventana_Marco1, width= 10)
				Dato.grid(row = fil, column = col)
				fila.append(Dato)
			Matriz.append(fila)
		
		Ventana_GuardaMatriz = Button(self.Ventana_Marco2, text = "Guardar matriz", command = lambda:self.Guardar_Matriz(Matriz))
		Ventana_GuardaMatriz.grid(row = 0, column =0)

		Ventana_EtiqVecIni = Label(self.Ventana_Marco4, text='¿Tienes un vector inicial?', font=('Calibri', 12), bg='bisque2')
		Ventana_EtiqVecIni.grid(row=1, column=0)
		Ventana_BotonCrear = Button(self.Ventana_Marco4, text = 'Si', command = lambda:self.Vector_Inicial())
		Ventana_BotonCrear.grid(row = 1, column = 1, padx = 20)
	
	def Guardar_Matriz(self, Datos):

		self.letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

		self.Matrix1 = []
		for i in range(self.tama1):
			row = []
			for j in range(self.tama1):
				try:
					value = float(Datos[i][j].get())
				except:
					messagebox.showerror("Error", "Los datos de la matriz deben ser números.")
					return
				row.append(float(value))
			self.Matrix1.append(row)
		
		for i in range(self.tama1):
			suma_fila = sum(self.Matrix1[i])
			if suma_fila != 1:
				messagebox.showerror("Error", "La fila {} (letra {}) no suma 1.".format(i + 1, self.letras[i]))
				return
			
		tk.Label(self.Ventana_Marco3, text="Matriz de transición", bg = 'bisque2').grid(row=0, column=0, padx=5, pady=5)

		for j in range(self.tama1):
			label = tk.Label(self.Ventana_Marco3, text=self.letras[j], bg='bisque2')
			label.grid(row=0, column=j+1, padx=5, pady=5)

		for i in range(len(self.Matrix1)):
			label = tk.Label(self.Ventana_Marco3, text=self.letras[i], bg='bisque2')
			label.grid(row=i+1, column=0, padx=5, pady=5)
			
			for j in range(len(self.Matrix1[i])):
				Imp = tk.Label(self.Ventana_Marco3, text=self.Matrix1[i][j], bg='bisque2')
				Imp.grid(row=i+1, column=j+1, padx=5, pady=5)

		self.Matrix = np.array(self.Matrix1)
		self.matriz_vec = np.array(self.Matrix1)

		Ventana_EtiqPeri = Label(self.Ventana_Marco14, text='Numero de periodos a ver de la matriz de transición:', font=('Calibri', 12), bg='bisque2')
		Ventana_EtiqPeri.grid(row=1, column=0)
		Ventana_ValorPe = StringVar()
		Ventana_EntradaPeri = Entry(self.Ventana_Marco14, textvar=Ventana_ValorPe, width='10', font=('Calibri', 12))
		Ventana_EntradaPeri.grid(row=1, column=1, padx=20)
		Ventana_BotonNumPe = Button(self.Ventana_Marco14, text = 'Ver Resultado Paso a Paso', command = lambda:self.Ver_PeriodosPaso(Ventana_ValorPe))
		Ventana_BotonNumPe.grid(row = 1, column = 2, padx = 20)
		Ventana_BotonNumPe2 = Button(self.Ventana_Marco14, text = 'Ver Resultado Directo', command = lambda:self.Ver_PeriodosDirec(Ventana_ValorPe))
		Ventana_BotonNumPe2.grid(row = 1, column = 3, padx = 20)

		Ventana_EtiqPeri = Label(self.Ventana_Marco11, text='Calcular Estado Estable:', font=('Calibri', 12), bg='bisque2')
		Ventana_EtiqPeri.grid(row=1, column=0)
		Ventana_BotonEsta = Button(self.Ventana_Marco11, text = 'Ver Resultado Paso a Paso', command = lambda:self.VerPasoEstado_Estable())
		Ventana_BotonEsta.grid(row = 1, column = 1, padx = 20)
		Ventana_BotonEsta = Button(self.Ventana_Marco11, text = 'Ver Resultado Directo', command = lambda:self.VerDirecEstado_Estable())
		Ventana_BotonEsta.grid(row = 1, column = 2, padx = 20)
		
	def Ver_PeriodosPaso(self, Periodos):
		NumPeri = Periodos.get()
		try:
			Numero = int(NumPeri)
		except:
			messagebox.showerror("Error", "Debe ser un número entero.")
			return
		
		def mulMatriz(matriz, veces):
			filas = len(matriz)
			columnas = len(matriz[0])

			resultado = matriz

			for v in range(veces - 1):

				matriz_peri = []

				for i in range(filas):
					fila = []
					for j in range(columnas):
						elemento = 0
						for k in range(filas):
							elemento += matriz[i][k] * resultado[k][j]
						fila.append(elemento)
					matriz_peri.append(fila)

				resultado = matriz_peri

			return resultado

		tk.Label(self.Ventana_Marco16, text="RESULTADO PASO A PASO", bg = 'bisque2').grid(row=1, column=0, padx=5, pady=5)

		for i in range(2, 1 + Numero):
			tk.Label(self.Ventana_Marco16, text="Periodo^" + str(i), bg='bisque2').grid(row=(i-1)*4-2, column=0, padx=5, pady=5)
			
			matriz_Perio = mulMatriz(self.Matrix, i)

			matriz_texto = ""
			for fila in matriz_Perio:
				matriz_texto += "  ".join("{:.8f}".format(elemento) for elemento in fila) + "\n"

			matriz_Etiq = tk.Label(self.Ventana_Marco16, text=matriz_texto, bg='bisque2', justify="left")
			matriz_Etiq.grid(row=(i-1)*4-1, column=0, padx=5, pady=5)

			enunciados = []
			n_filas = len(matriz_Perio)
			n_columnas = len(matriz_Perio[0])

			for j in range(n_filas):
				for k in range(n_columnas):
					letra_1 = self.letras[j]
					letra_2 = self.letras[k]
					valor = matriz_Perio[j][k]
					enunciado = f"{letra_1} a {letra_2}: {round(valor, 10)}"
					enunciados.append(enunciado)

			matriz_texto = ""
			for enunciado in enunciados:
				matriz_texto += enunciado + "\n"

			matriz_Etiq = tk.Label(self.Ventana_Marco16, text=matriz_texto, bg='bisque2', justify="left")
			matriz_Etiq.grid(row=(i-1)*4, column=0, padx=5, pady=5)

	def Ver_PeriodosDirec(self, Periodos):
		NumPeri = Periodos.get()
		try:
			Numero = int(NumPeri)
		except:
			messagebox.showerror("Error", "Debe ser un número entero.")
			return
		
		def mulMatriz(matriz, veces):
			filas = len(matriz)
			columnas = len(matriz[0])

			resultado = matriz

			for v in range(veces - 1):

				matriz_peri = []

				for i in range(filas):
					fila = []
					for j in range(columnas):
						elemento = 0
						for k in range(filas):
							elemento += matriz[i][k] * resultado[k][j]
						fila.append(elemento)
					matriz_peri.append(fila)

				resultado = matriz_peri

			return resultado

		tk.Label(self.Ventana_Marco15, text="RESULTADO DIRECTO", bg = 'bisque2').grid(row=0, column=0, padx=5, pady=5)
		tk.Label(self.Ventana_Marco15, text="Periodo^" + str(Numero), bg='bisque2').grid(row=1, column=0, padx=5, pady=5)
		for i in range(2, 1 + Numero):
			matriz_Perio = mulMatriz(self.Matrix, i)

			matriz_texto = ""
			for fila in matriz_Perio:
				matriz_texto += "  ".join("{:.8f}".format(elemento) for elemento in fila) + "\n"
			
		matriz_Etiq  = tk.Label(self.Ventana_Marco15, text=matriz_texto, bg='bisque2', justify="left")
		matriz_Etiq .grid(row=2, column=0, padx=5, pady=5)

		enunciados = []
		n_filas = len(matriz_Perio)
		n_columnas = len(matriz_Perio[0])

		for i in range(n_filas):
			for j in range(n_columnas):
				letra_1 = self.letras[i]
				letra_2 = self.letras[j]
				valor = matriz_Perio[i][j]
				enunciado = f"{letra_1} a {letra_2}: {round(valor,10)}"
				enunciados.append(enunciado)

		matriz_texto = ""
		for i in enunciados:
			matriz_texto += i + "\n"
		
		matriz_Etiq  = tk.Label(self.Ventana_Marco15, text=matriz_texto, bg='bisque2', justify="left")
		matriz_Etiq .grid(row=3, column=0, padx=5, pady=5)
	
	def VerPasoEstado_Estable(self):
		def transpo_matriz(matriz):
			filas = len(matriz)
			columnas = len(matriz[0])

			matriz_transpuesta = []

			for j in range(columnas):
				fila_transpuesta = []
				for i in range(filas):
					fila_transpuesta.append(matriz[i][j])
				matriz_transpuesta.append(fila_transpuesta)

			return matriz_transpuesta

		self.Matriz_Transp = transpo_matriz(self.Matrix)
		tk.Label(self.Ventana_Marco13, text="RESULTADO PASO A PASO", bg = 'bisque2').grid(row=0, column=0, padx=5, pady=5)
		tk.Label(self.Ventana_Marco13, text="Matriz transpuesta", bg='bisque2').grid(row=1, column=0, padx=5, pady=5)

		matriz_trans = ""
		for fila in self.Matriz_Transp:
			matriz_trans += "	".join("{:.3f}".format(elemento) for elemento in fila) + "\n"

		matriz_Etiq = tk.Label(self.Ventana_Marco13, text=matriz_trans, bg='bisque2', justify="left")
		matriz_Etiq.grid(row=2, column=0, padx=5, pady=5)

		for i, dia in enumerate(self.Matriz_Transp):
			self.Matriz_Transp[i][i] -= 1

		tk.Label(self.Ventana_Marco13, text="Resta de -1 a la diagonal principal", bg='bisque2').grid(row=3, column=0, padx=5, pady=5)
		matriz_trans = ""
		for fila in self.Matriz_Transp:
			matriz_trans += "    ".join("{:.3f}".format(elemento) for elemento in fila) + "\n"

		matriz_Etiq = tk.Label(self.Ventana_Marco13, text=matriz_trans, bg='bisque2', justify="left")
		matriz_Etiq.grid(row=4, column=0, padx=5, pady=5)
		
		tk.Label(self.Ventana_Marco13, text="Agregacion de valores para calcular matriz inversa", bg = 'bisque2').grid(row=5, column=0, padx=5, pady=5)
		filas = len(self.Matriz_Transp)
		columnas = len(self.Matriz_Transp[0])

		Matriz_valoAgr = []
		for i in range(filas + 1):
			fila = []
			for j in range(columnas + 1):
				if i < filas and j < columnas:
					fila.append(self.Matriz_Transp[i][j])
				elif i < filas and j == columnas:
					fila.append(1)
				elif i == filas and j < columnas:
					fila.append(1)
				elif i == filas and j == columnas:
					fila.append(0)
			Matriz_valoAgr.append(fila)

		matriz_agrega = ""
		for fila in Matriz_valoAgr:
			matriz_agrega += "    ".join("{:.3f}".format(elemento) for elemento in fila) + "\n"
		matriz_Etiq = tk.Label(self.Ventana_Marco13, text=matriz_agrega, bg='bisque2', justify="left")
		matriz_Etiq.grid(row=6, column=0, padx=5, pady=5)

		
		tk.Label(self.Ventana_Marco13, text="Agregacion de valores para calcular matriz inversa", bg='bisque2').grid(row=7, column=0, padx=5, pady=5)
		Matriz_inversa = np.linalg.inv(Matriz_valoAgr)
		matriz_in = ""
		for fila in Matriz_inversa:
			matriz_in += "    ".join("{:.8f}".format(elemento) for elemento in fila) + "\n"

		matriz_Etiq = tk.Label(self.Ventana_Marco13, text=matriz_in, bg='bisque2', justify="left")
		matriz_Etiq.grid(row=8, column=0, padx=5, pady=5)

		Matriz_valoAgr1 = np.array(Matriz_valoAgr)
		filas, columnas = Matriz_valoAgr1.shape
		Matriz_valoAgr2 = np.zeros((filas, columnas + 1))
		Matriz_valoAgr2[:, :-1] = Matriz_valoAgr
		Matriz_valoAgr2[:-1, -1] = 0
		Matriz_valoAgr2[-1, -1] = 1
		tk.Label(self.Ventana_Marco13, text="Agregacion de valores para calcular el estado estable", bg='bisque2').grid(row=9, column=0, padx=5, pady=5)
		matriz_agrega2 = ""
		for fila in Matriz_valoAgr2:
			matriz_agrega2 += "    ".join("{:.3f}".format(elemento) for elemento in fila) + "\n"
		matriz_Etiq = tk.Label(self.Ventana_Marco13, text=matriz_agrega2, bg='bisque2', justify="left")
		matriz_Etiq.grid(row=10, column=0, padx=5, pady=5)

		tk.Label(self.Ventana_Marco13, text="Estado Estable: ", bg='bisque2').grid(row=11, column=0, padx=5, pady=5)

		ultimaCol = [fila[-1] for fila in Matriz_valoAgr2]
		Estado_Estable = []
		for fila in Matriz_inversa:
			suma = 0
			for i in range(len(fila)):
				suma += fila[i] * ultimaCol[i]
			Estado_Estable.append(suma)

		vec_esta = " ".join("{}  {:.8f}  ".format(letra, valor) for letra, valor in zip(self.letras, Estado_Estable))
		ve_es = tk.Label(self.Ventana_Marco13, text=vec_esta, bg='bisque2', justify="left")
		ve_es.grid(row=12, column=0, padx=5, pady=5)
	
	def VerDirecEstado_Estable(self):
		def transpo_matriz(matriz):
			filas = len(matriz)
			columnas = len(matriz[0])

			matriz_transpuesta = []

			for j in range(columnas):
				fila_transpuesta = []
				for i in range(filas):
					fila_transpuesta.append(matriz[i][j])
				matriz_transpuesta.append(fila_transpuesta)

			return matriz_transpuesta

		self.Matriz_Transp = transpo_matriz(self.Matrix)
		

		for i, dia in enumerate(self.Matriz_Transp):
			self.Matriz_Transp[i][i] -= 1
		
		filas = len(self.Matriz_Transp)
		columnas = len(self.Matriz_Transp[0])

		Matriz_valoAgr = []
		for i in range(filas + 1):
			fila = []
			for j in range(columnas + 1):
				if i < filas and j < columnas:
					fila.append(self.Matriz_Transp[i][j])
				elif i < filas and j == columnas:
					fila.append(1)
				elif i == filas and j < columnas:
					fila.append(1)
				elif i == filas and j == columnas:
					fila.append(0)
			Matriz_valoAgr.append(fila)

		Matriz_inversa = np.linalg.inv(Matriz_valoAgr)

		Matriz_valoAgr1 = np.array(Matriz_valoAgr)
		filas, columnas = Matriz_valoAgr1.shape
		Matriz_valoAgr2 = np.zeros((filas, columnas + 1))
		Matriz_valoAgr2[:, :-1] = Matriz_valoAgr
		Matriz_valoAgr2[:-1, -1] = 0
		Matriz_valoAgr2[-1, -1] = 1

		tk.Label(self.Ventana_Marco12, text="RESULTADO DIRECTO", bg = 'bisque2').grid(row=0, column=0, padx=5, pady=5)
		tk.Label(self.Ventana_Marco12, text="Estado Estable: ", bg='bisque2').grid(row=1, column=0, padx=5, pady=5)

		ultimaCol = [fila[-1] for fila in Matriz_valoAgr2]
		Estado_Estable = []
		for fila in Matriz_inversa:
			suma = 0
			for i in range(len(fila)):
				suma += fila[i] * ultimaCol[i]
			Estado_Estable.append(suma)

		vector_estable_texto = " ".join("{}  {:.8f}  ".format(letra, valor) for letra, valor in zip(self.letras, Estado_Estable))
		vector_estable_label = tk.Label(self.Ventana_Marco12, text=vector_estable_texto, bg='bisque2', justify="left")
		vector_estable_label.grid(row=2, column=0, padx=5, pady=5)
		
	def Vector_Inicial(self):

		Vector = []
		for fil in range(1):
			fila= []
			for col in range(self.tama1):
				Dato = Entry(self.Ventana_Marco5, width= 10)
				Dato.grid(row = fil, column = col)
				fila.append(Dato)
			Vector.append(fila)

		Ventana_BotonVec = Button(self.Ventana_Marco6, text = 'Guardar Vector', command = lambda:self.Ver_Vector_Peri(Vector))
		Ventana_BotonVec.grid(row = 1, column = 0, padx = 20)

		Ventana_EtiqPeri = Label(self.Ventana_Marco8, text='Numero de distribuciones a ver del vector inicial:', font=('Calibri', 12), bg='bisque2')
		Ventana_EtiqPeri.grid(row=1, column=0)
		Ventana_ValorN = StringVar()
		Ventana_EntradaN = Entry(self.Ventana_Marco8, textvar=Ventana_ValorN, width='10', font=('Calibri', 12))
		Ventana_EntradaN.grid(row=1, column=1, padx=20)
		Ventana_BotonN = Button(self.Ventana_Marco8, text = 'Ver Resultado Paso a Paso', command = lambda:self.VerPaso_Vector(Ventana_ValorN))
		Ventana_BotonN.grid(row = 1, column = 2, padx = 20)
		Ventana_BotonN = Button(self.Ventana_Marco8, text = 'Ver Resultado Directo', command = lambda:self.VerDirec_Vector(Ventana_ValorN))
		Ventana_BotonN.grid(row = 1, column = 3, padx = 20)

	def Ver_Vector_Peri(self, vector):
		self.VectorIni = []
		for i in range(1):
			row = []
			for j in range(self.tama1):
				try:
					value = float(vector[i][j].get())
				except:
					messagebox.showerror("Error", "Los datos del vector deben ser números.")
					return
				row.append(float(value))
			self.VectorIni.append(row)

		for i in range(1):
			suma_fila = sum(self.VectorIni[i])
			if suma_fila != 1:
				messagebox.showerror("Error", "La fila {} no suma 1.".format(i + 1))
				return
		
		self.VectorInici = np.array(self.VectorIni)
		self.VectorInici1 = np.array(self.VectorIni)
		self.VectorInici2 = np.array(self.VectorIni)

		tk.Label(self.Ventana_Marco7, text="Vector inicial", bg = 'bisque2').grid(row=1, column=0, padx=5, pady=5)
		for i in range(len(self.VectorInici)):
			for j in range(len(self.VectorInici[i])):
				label = tk.Label(self.Ventana_Marco7, text=self.letras[j], bg='bisque2')
				label.grid(row=0, column=j+1, padx=5, pady=5)
				Imp = Label(self.Ventana_Marco7, text=self.VectorInici[i][j], bg = 'bisque2')
				Imp.grid(row=i+1, column=j+1, padx=5, pady=5)
		

	def VerPaso_Vector(self,numero):
		Num = numero.get()
		try:
			Numero = int(Num)
		except:
			messagebox.showerror("Error", "Debe ser un número entero.")
			return
			
		tk.Label(self.Ventana_Marco10, text="RESULTADO PASO A PASO", bg = 'bisque2').grid(row=0, column=0, padx=5, pady=5)
		for i in range(1,Numero+1):  
			tk.Label(self.Ventana_Marco10, text="P" + str(i), bg='bisque2').grid(row=2*i-1, column=0, padx=5, pady=5)
			vector_peri = np.dot(self.VectorInici1, self.matriz_vec)
			self.VectorInici1 = vector_peri

			matriz_Ini = ""
			for fila in self.VectorInici1:
				matriz_Ini += "    ".join("{}  {:.8f}  ".format(letra, valor) for letra, valor in zip(self.letras, fila))
				
			matriz_Etiq = tk.Label(self.Ventana_Marco10, text=matriz_Ini, bg='bisque2', justify="left")
			matriz_Etiq.grid(row=2*i, column=0, padx=5, pady=5)
	
	def VerDirec_Vector(self,numero):
		Num = numero.get()
		try:
			Numero = int(Num)
		except:
			messagebox.showerror("Error", "Debe ser un número entero.")
			return
		
		tk.Label(self.Ventana_Marco9, text="RESULTADO DIRECTO", bg = 'bisque2').grid(row=0, column=0, padx=5, pady=5)
		tk.Label(self.Ventana_Marco9, text="P" + str(Numero), bg='bisque2').grid(row=1, column=0, padx=5, pady=5)
		for i in range(1,Numero+1):  
			vector_peri = np.dot(self.VectorInici2, self.matriz_vec)
			self.VectorInici2 = vector_peri

			matriz_Ini2 = ""
			for fila in self.VectorInici2:
				matriz_Ini2 += "    ".join("{}  {:.8f}  ".format(letra, valor) for letra, valor in zip(self.letras, fila))
				
			matriz_Etiq = tk.Label(self.Ventana_Marco9, text=matriz_Ini2, bg='bisque2', justify="left")
			matriz_Etiq.grid(row=2, column=0, padx=5, pady=5)
principal = Ventana()
