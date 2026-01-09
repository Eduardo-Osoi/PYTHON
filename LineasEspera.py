import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

class Ventana:
    def __init__(self):
        self.Ventana = Tk()

        self.Ventana.geometry('900x600')

        self.Ventana.title('Investigación de Operaciones')
        self.Ventana.config(bg='bisque2')

        self.canvas = Canvas(self.Ventana, bg='bisque2')
        self.canvas.grid(row=0, column=0, sticky="nsew")

        Ventana_Marco0 = Frame(self.canvas, bg="bisque2")
        Ventana_Marco0.config(padx='10', pady='10', borderwidth=1, relief='ridge')
        self.canvas.create_window((0, 0), window=Ventana_Marco0, anchor="nw")

        Ventana_Marco1 = Frame(Ventana_Marco0, bg="bisque2")
        Ventana_Marco1.config(padx='10', pady='10', borderwidth=1, relief='ridge')
        self.canvas.create_window((1, 0), window=Ventana_Marco0, anchor="nw")

        self.scrollbar = Scrollbar(self.Ventana, orient="vertical", command=self.canvas.yview)
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
        self.Ventana_Marco2.grid(row=3, column=2, padx=10, pady=20)
        self.Ventana_Marco3 = Frame(Ventana_Marco0, bg="bisque2")
        self.Ventana_Marco3.grid(row=4, column=2, padx=10, pady=20)
        self.Ventana_Marco4 = Frame(Ventana_Marco0, bg="bisque2")
        self.Ventana_Marco4.grid(row=5, column=2, padx=10, pady=20)

        Ventana_EtiqLamda= Label(Ventana_Marco, text='Tasa media de llegadas en unidad de tiempo λ:', font=('Calibri', 12), bg='bisque2')
        Ventana_EtiqLamda.grid(row=1, column=0)
        Ventana_ValorLa = StringVar()
        Ventana_EntradaLAM = Entry(Ventana_Marco, textvar=Ventana_ValorLa, width='10', font=('Calibri', 12))
        Ventana_EntradaLAM.grid(row=1, column=1, padx=20)
        Ventana_ValorHoraMin1 = StringVar()
        Ventana_Lamda = ttk.Combobox(Ventana_Marco,textvariable = Ventana_ValorHoraMin1, font=('Calibri', 12), state='readonly')
        Ventana_Lamda['values'] = ('horas','minutos')
        Ventana_Lamda.current(0)
        Ventana_Lamda.grid(row=1, column=2, padx=10)

        Ventana_EtiqMiu= Label(Ventana_Marco, text='Tasa media de servicio por canal de servicio en unidad de tiempo μ:', font=('Calibri', 12), bg='bisque2')
        Ventana_EtiqMiu.grid(row=2, column=0)
        Ventana_ValorM = StringVar()
        Ventana_EntradaMU = Entry(Ventana_Marco, textvar=Ventana_ValorM, width='10', font=('Calibri', 12))
        Ventana_EntradaMU.grid(row=2, column=1, padx=20)
        Ventana_ValorHoraMin2 = StringVar()
        Ventana_Mu = ttk.Combobox(Ventana_Marco,textvariable =Ventana_ValorHoraMin2, font=('Calibri', 12), state='readonly')
        Ventana_Mu['values'] = ('horas','minutos')
        Ventana_Mu.current(0)
        Ventana_Mu.grid(row=2, column=2, padx=10)

        Ventana_EtiqServi= Label(Ventana_Marco, text='Numero de servidores o canales de servicio s:', font=('Calibri', 12), bg='bisque2')
        Ventana_EtiqServi.grid(row=3, column=0)
        Ventana_ValorS = StringVar()
        Ventana_EntradaSER = Entry(Ventana_Marco, textvar=Ventana_ValorS, width='10', font=('Calibri', 12))
        Ventana_EntradaSER.grid(row=3, column=1, padx=20)
        Ventana_EtiqServi= Label(Ventana_Marco, text='Servidores', font=('Calibri', 12), bg='bisque2')
        Ventana_EtiqServi.grid(row=3, column=2)

        Ventana_EtiqClient= Label(Ventana_Marco, text='Clientes N:', font=('Calibri', 12), bg='bisque2')
        Ventana_EtiqClient.grid(row=4, column=0)
        Ventana_ValorC = StringVar()
        Ventana_EntradaCLI = Entry(Ventana_Marco, textvar=Ventana_ValorC, width='10', font=('Calibri', 12))
        Ventana_EntradaCLI.grid(row=4, column=1, padx=20)

        Ventana_BotonCalcu = Button(Ventana_Marco, text = 'Calcular', command = lambda:self.Calcular(Ventana_EntradaLAM, Ventana_EntradaMU, Ventana_EntradaSER, Ventana_ValorC, Ventana_ValorHoraMin1, Ventana_ValorHoraMin2))
        Ventana_BotonCalcu.grid(row = 1, column = 3, padx = 20)
    
        self.Ventana.mainloop()


    def Calcular(self, lamda, mu, s, n, hora_min1, hora_min2):
        lamdaEn = lamda.get()
        muEn = mu.get()
        sEn = s.get()
        nEn = n.get()
        horaymin1 = hora_min1.get()
        horaymin2 = hora_min2.get()
        try:
            if horaymin1 == 'minutos':
                L = float(lamdaEn)/60
            if horaymin2 == 'minutos':	
                M = float(muEn)/60
            if horaymin1 == 'horas':
                L = float(lamdaEn)
            if horaymin2 == 'horas':	
                M = float(muEn)
            S = int(sEn)
            if nEn == "":
                N = None
            else:
                N = int(nEn)
        except:
            messagebox.showerror("Error", "Los valores deben ser números enteros.")
            return

        def Rho(S, L, M):
            if S * M > L:
                return L / (S * M)
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0

        def Factorial(n):
            facto = 1
            for i in range(1, n+1):
                facto = facto * i
            return facto

        def P0(S, L, M):
            if S * M > L:
                suma = 0
                for i in range(S):
                    suma = suma + (L / M) ** i / Factorial(i)
                return 1 / (suma + ((L / M) ** S / Factorial(S)) * (1 / (1 - Rho(S, L, M))))
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0
        
        def Lq(S, L, M):
            if S * M > L:
                return ((L / M) ** S * L * M * P0(S, L, M)) / (Factorial(S - 1) * (S * M - L) ** 2)
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0

        def Ls(S, L, M):
            if S * M > L:
                return Lq(S, L, M) + L / M
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0

        def Wq(S, L, M):
            if S * M > L:
                return Lq(S, L, M) / L
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0

        def Ws(S, L, M):
            if S * M > L:
                return Wq(S, L, M) + (1 / M)
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0

        def Pn(S, L, M, n):
            if S * M > L:
                if n <= S:
                    return ((L / M) ** n) * P0(S, L, M) / Factorial(n)
                else:
                    return ((L / M) ** n) * P0(S, L, M) / (Factorial(S) * S ** (n - S))
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0

        def Pw(S, L, M):
            if S * M > L:
                return (1 / Factorial(S)) * ((L / M) ** S) * ((S * M) / (S * M - L)) * P0(S, L, M)
            else:
                messagebox.showerror("Error", "Sistema Inestable")
                return 0


        Etiqueta_p = tk.Label(self.Ventana_Marco1, text='P: {:.3f}'.format(round(Rho(S,L,M)*100,2))+'%', bg='bisque2', justify="left")
        Etiqueta_p.grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.Ventana_Marco1, text="Porcentaje de ocupacion del sistema", bg='bisque2').grid(row=2, column=0, padx=5, pady=5)

        Etiqueta_p0 = tk.Label(self.Ventana_Marco1, text='P0: {:.3f}'.format(round(P0(S,L,M)*100,2))+'%', bg='bisque2', justify="left")
        Etiqueta_p0.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.Ventana_Marco1, text="Probabilidad de sistema vacio", bg='bisque2').grid(row=2, column=1, padx=5, pady=5)

        Etiqueta_Lq = tk.Label(self.Ventana_Marco2, text='Lq: {:.10f}'.format(Lq(S,L,M))+' Clientes', bg='bisque2', justify="left")
        Etiqueta_Lq.grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.Ventana_Marco2, text="Cantidad promedio de clientes en la cola", bg='bisque2').grid(row=2, column=0, padx=5, pady=5)

        Etiqueta_Ls = tk.Label(self.Ventana_Marco2, text='Ls: {:.10f}'.format(Ls(S,L,M))+' Clientes', bg='bisque2', justify="left")
        Etiqueta_Ls.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.Ventana_Marco2, text="Cantidad promedio de clientes en el sistema", bg='bisque2').grid(row=2, column=1, padx=5, pady=5)

        Etiqueta_wq = tk.Label(self.Ventana_Marco3, text='Wq: {:.10f} Horas -> {:.10f} Minutos'.format(Wq(S,L,M), Wq(S,L,M)*60), bg='bisque2', justify="left")
        Etiqueta_wq.grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.Ventana_Marco3, text="Tiempo promedio de espera en la fila", bg='bisque2').grid(row=2, column=0, padx=5, pady=5)

        Etiqueta_ws = tk.Label(self.Ventana_Marco3, text='Ws: {:.10f} Horas -> {:.10f} Minutos'.format(Ws(S,L,M),Ws(S,L,M)*60), bg='bisque2', justify="left")
        Etiqueta_ws.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.Ventana_Marco3, text="Tiempo promedio de permanencia en el sistema", bg='bisque2').grid(row=2, column=1, padx=5, pady=5)

        if N is None:
            Etiqueta_pn = tk.Label(self.Ventana_Marco4, text='Pn: NANN', bg='bisque2', justify="left")
            Etiqueta_pn.grid(row=1, column=0, padx=5, pady=5)
            tk.Label(self.Ventana_Marco4, text='Probabilidad de que haya "n" clientes en el sistema', bg='bisque2').grid(row=2, column=0, padx=5, pady=5)
        else:
            Etiqueta_pn = tk.Label(self.Ventana_Marco4, text='Pn: {:.3f}'.format(round(Pn(S, L, M, N)* 100, 2))+ '%', bg='bisque2', justify="left")
            Etiqueta_pn.grid(row=1, column=0, padx=5, pady=5)
            tk.Label(self.Ventana_Marco4, text='Probabilidad de que haya "n" clientes en el sistema', bg='bisque2').grid(row=2, column=0, padx=5, pady=5)

        Etiqueta_pw = tk.Label(self.Ventana_Marco4, text='Pw: {:.3f}'.format(round(Pw(S,L,M)*100,2))+'%', bg='bisque2', justify="left")
        Etiqueta_pw.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.Ventana_Marco4, text="Probabilidad de que un cliente tenga que esperar", bg='bisque2').grid(row=2, column=1, padx=5, pady=5)

principal = Ventana()