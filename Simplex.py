# -*- coding: utf-8 -*-
"""
Editor de Spyder

By Cepetro.
"""
import math 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from random import randrange




#renglonPresentacion construlle el i-esimo renglon da la tabla simplex
def construccionRenglon(matrizActividades,vecDispo,n,m,I,faseDoble):
    """
    Se inicializa el renglon co un primer elemento 0 
                    => (0)
    """
    renglon=[0]
    """
    Se agrega n veces el i-esimo elemento del I-esimo renglon de la matriz 
    de actividades 
                    =>(0,aI1,aI2,...,aIn)
    """
    for i in range(n):
        renglon.append(matrizActividades[I][i])
    """
    Se agregan m ceros despies de los n elementos agregados y un 1 en la posicion I
                    =>((0,aI1,aI2,...,aIn,0,...,1,...,0)
    """
    
    for i in range(faseDoble):
        for j in range(m):
            if I==j:
                if faseDoble==1:
                    renglon.append(1)
                else:
                    if i==0:
                        renglon.append(-1)
                    else:
                        renglon.append(1)
            else:
                renglon.append(0)
    """
    Se agregan el elemento I-esimo del vector de disponibilidad en la ultima posicion
                    =>((0,aI1,aI2,...,aIn,0,...,0,bI)
    """
    renglon.append(vecDispo[I])
    return renglon
    
#Construccion de la tabla del metodo simplex
def construccionTabla(matrizActividades,Zopt,n,m,vecDispo,faseDoble):
    Tabla=[]
    """
    Se agrega el primer renglon con m+1 ceros al final
    Zopt=(1,c1,c2,...,cn,0,...0)
    """
    renglon=[1]
    if faseDoble==1:
        for i in range(n):
            renglon.append(-Zopt[i])
        for i in range((m)+1):
            renglon.append(0)
        Tabla.append(renglon)
    else:
        for i in range(n):
            renglon.append(0)
        for i in range((m)):
            renglon.append(0)
        for i in range((m)):
            renglon.append(1)
        renglon.append(0)
        Tabla.append(renglon)   
    """ 
    Se agrega el i-esimo renglon con m ceros al final y 1 en la i-esima posicion 
    despues del n-simo termino y un cero en la primera posicion
    Renglon = (0,ai1,ai2,...,ain,0,...,1,...,0,bi)
    """
    for i in range(m):
        Tabla.append(construccionRenglon(matrizActividades,vecDispo,n,m,i,faseDoble)) 

    return Tabla
 
def Ajustar(matrizActividades,vecDispo,iguales,n,m,faseDoble):
    AUXmatrizActividades=[]
    AUXvecDispo=[]
    AUXm=m
    for i in range(m):
        if iguales[i]==0:
            auxmatrizActividades=[]
            for j in range(n):
                auxmatrizActividades.append(-matrizActividades[i][j])
            AUXvecDispo.append(-vecDispo[i])
            AUXmatrizActividades.append(auxmatrizActividades)
            auxmatrizActividades=[]
            for j in range(n):
                auxmatrizActividades.append(matrizActividades[i][j])
            AUXvecDispo.append(vecDispo[i])
            AUXmatrizActividades.append(auxmatrizActividades)
            AUXm=m+1                
        elif iguales[i]== -1:
            if faseDoble == 1:
                AUXmatrizActividades.append(matrizActividades[i])
                AUXvecDispo.append(vecDispo[i])
            else:
                for j in range(n):
                    AUXmatrizActividades.append(-matrizActividades[i][j])
                    AUXvecDispo.append(-vecDispo[i])
        elif iguales[i] == 1:
            if faseDoble == 2:
                AUXmatrizActividades.append(matrizActividades[i])
                AUXvecDispo.append(vecDispo[i])
            else:
                for j in range(n):
                    AUXmatrizActividades.append(-matrizActividades[i][j])
                    AUXvecDispo.append(-vecDispo[i])            
        
    return AUXmatrizActividades, AUXvecDispo,AUXm
    

def inicializaSimplex(matrizActividades,Zopt,n,m,vecDispo,iguales,faseDoble):
    
    names_Image=[]        
    """
    Se le cambian todas las igualdades por dos desigualdades y m aumenta en 1
    por cada cambio
    """
    matrizActividades,vecDispo,m=Ajustar(matrizActividades,vecDispo,iguales,n,m,faseDoble)
    """
    Se toman los valores de la matriz de actividades, el vector de disponibilidad
    y la función objetivo para construir la tabla simplex
    """
    Tabla=construccionTabla(matrizActividades,Zopt,n,m,vecDispo,faseDoble)
    
    if faseDoble==1:
        return Simplex(Tabla, n, m,faseDoble,names_Image)
    else:
        return DobleFase(Tabla, n, m,faseDoble,Zopt,names_Image)


def Imprimir_Tabla(Tabla,n,m,faseDoble,H,Resultados,regPivote,names_Image):
    ran=randrange(10000000000000000000000000000000000000000000)
    nameRenglones=[]
    
    for i in range(m+1):
        if i ==0:
            nameRenglones.append("Z")
        else:
            nameRenglones.append("X"+str(i))
    dic={}
    for i in range(m+1):
        dic.update({nameRenglones[i]:Tabla[i]})
    df=pd.DataFrame(dic)
    print(df.transpose())
    name='DataFrame_'+str(ran)+'.png'
    names_Image.append(name)
    plt.figure(facecolor='w', edgecolor='k')
    sns.heatmap(df.transpose(), annot=True, cmap='viridis', cbar=False)
    plt.savefig(name)
        
    if regPivote>0:
      ran=randrange(10000000000000000000000000000000000000000000)
      name='DataFrame_'+str(ran)+'.png'
      names_Image.append(name)
      
      dic.update({'Renglon salida':regPivote})
      df=pd.DataFrame(dic)
      plt.figure(facecolor='w', edgecolor='k')
      sns.heatmap(df, annot=True, cmap='viridis', cbar=True)
      plt.savefig(name)
      
    
    return names_Image

def Restricciones(Tabla,fase_Doble,m,n):
    
    if fase_Doble==1:
        Zmin = sorted(Tabla[0])
    else:
        Zmin = [Tabla[0][n+(2*m)]]
        
    return Zmin

def Simplex(Tabla,n,m,faseDoble,names_Image):
    B=[]
    auxB=[]
    auxZ=[]
    Resultados=[]

        
    for i in range(m+1):
        Resultados.append(0)        
    Zmin =Restricciones(Tabla,1,m,n)
    for i in range(m):
        auxz=[]
        for j in range((m)+n+1):
            auxz.append(0)
        auxZ.append(auxz)
    H=0
    AuxTabla=[]
    for i in range(m+1):
        auxTabla=[]
        for j in range((m)+n+2):
            auxTabla.append(str(Tabla[i][j]))
        AuxTabla.append(auxTabla)
    names_Image=Imprimir_Tabla(Tabla,n,m,1,H,Resultados,-1,names_Image)
    while Zmin[0] < 0:
        auxB=[]
        B=[]
        TablaControl=[]
        for i in range(m+1):                      
            auxTabla=[]
            for j in range(n+(m)+2):
                auxTabla.append(Tabla[i][j])                
            TablaControl.append(auxTabla)
        if Zmin[0] == Tabla[0][n+(m)+1]:
            aux1=Zmin[1]
        else:
            aux1=Zmin[0]
        for i in range(n+m+1):
            if Tabla[0][i]== aux1:
                colPivote = i
                break
        auxM=0
        for i in range(m+1):
            if i!=0:
                if Tabla[i][colPivote]>0:  
                    B.append(Tabla[i][(m)+n+1]/Tabla[i][colPivote])
                else:
                    B.append(math.inf)
                
                auxM=auxM+1
         
        auxB=sorted(B)
        if auxB[0]==math.inf:
            return auxB
        
        for i in range(auxM):
            if B[i] == auxB[0]:
                    regPivote=i+1
                    
        Resultados[regPivote]= colPivote   

        auxReg=Tabla[regPivote][colPivote]
        for i in range(n+(m)+2):
            Tabla[regPivote][i]=Tabla[regPivote][i]/auxReg
            
        for i in range(m+1):
            auxSimplex =Tabla[i][colPivote]
            for j in range(n+(m)+2):
                if i != regPivote:
                    Tabla[i][j]=Tabla[i][j]-(auxSimplex*Tabla[regPivote][j])
        Zmin = Restricciones(Tabla,1,m,n)
        H=H+1
        control=0
        for i in range(m+1):
            for j in range(n+(m)+2):
                if TablaControl[i][j]!=Tabla[i][j]:
                    control=1
        names_Image=Imprimir_Tabla(Tabla,n,m,1,H,colPivote,regPivote,names_Image)
        if control == 0:
            break
        if H == 100:
            break   
        
    Xi=[]
    for i in range(n):
        Xi.append(0)
    
    
    for i in range(m+1):
            if Resultados[i]!=0 and Resultados[i] < n+1 :
                Xi[Resultados[i]-1]=Tabla[i][n+m+1]                                         
    names_Image=Imprimir_Tabla(Tabla,n,m,1,H,Resultados,-1,names_Image)
    
    if faseDoble==1:
        return Xi,Tabla[0][n+m+1],names_Image
    else:
        return Xi,-Tabla[0][n+m+1],names_Image

def DobleFase(Tabla, n, m,faseDoble,Zopt,names_Image):
    B=[]
    auxB=[]
    auxZ=[]
    Resultados=[]
    for i in range(m+1):
        Resultados.append(0) 
    
    Zmin = Restricciones(Tabla,1,m,n)
    if Zmin[0]<0:
        zero=1
    else:
        zero=0
    
    
    Zmin = Restricciones(Tabla,faseDoble,m,n)
    
    for i in range(m+1):
        for j in range(n+(2*m)+2):
            if i!=0:
                Tabla[0][j]=Tabla[0][j] - Tabla[i][j]

    
    for i in range(m):
        auxz=[]
        for j in range((faseDoble*m)+n+1):
            auxz.append(0)
        auxZ.append(auxz)
    H=0
    AuxTabla=[]
    for i in range(m+1):
        auxTabla=[]
        for j in range((m*faseDoble)+n+2):
            auxTabla.append(str(Tabla[i][j]))
        AuxTabla.append(auxTabla)    
    names_Image=Imprimir_Tabla(Tabla,n,m,faseDoble,H,Resultados,-1,names_Image)
    while Zmin[0] != 0 or zero==1:
        auxB=[]
        B=[]
        TablaControl=[]
        for i in range(m+1):                      
            auxTabla=[]
            for j in range(n+(2*m)+2):
                auxTabla.append(Tabla[i][j])                
            TablaControl.append(auxTabla)
        
        aux = Restricciones(Tabla,1,m,n)
        if aux[0] == Tabla[0][n+(2*m)+1]:
            aux[0]=aux[1]

        for i in range(n+m):
            if Tabla[0][i]==aux[0]:
                colPivote = i
                break
        auxM=0
        for i in range(m+1):
            if i!=0:
                if Tabla[i][colPivote] > 0:  
                    B.append(Tabla[i][(faseDoble*m)+n+1]/Tabla[i][colPivote])
                else:
                    B.append(math.inf)
                
                auxM=auxM+1
         
        auxB=sorted(B)
         
        if auxB[0]==math.inf:
            return auxB
        
        for i in range(auxM):
            if B[i] == auxB[0]:
                    regPivote=i+1
        
        Resultados[regPivote]= colPivote            
        auxReg=Tabla[regPivote][colPivote]
        for i in range(n+(faseDoble*m)+2):
            Tabla[regPivote][i]=Tabla[regPivote][i]/auxReg
            
        for i in range(m+1):
            auxSimplex =Tabla[i][colPivote]
            for j in range(n+(faseDoble*m)+2):
                if i != regPivote:
                    Tabla[i][j]=Tabla[i][j]-(auxSimplex*Tabla[regPivote][j])
        aux = Restricciones(Tabla,1,m,n)
        if aux[0]<0:
            zero=1
        else:
            zero=0        
        Zmin = Restricciones(Tabla,faseDoble,m,n)
        H=H+1
        control=0
        for i in range(m+1):
            for j in range(n+(m*2)+2):
                if TablaControl[i][j]!=Tabla[i][j]:
                    control=1
        names_Image=Imprimir_Tabla(Tabla,n,m,faseDoble,H,Resultados,regPivote,names_Image)
        if control == 0:
            break
        if H == 100:
            break
                               
    AUXtabla=[] 
    for i in range(m+1):                      
        auxTabla=[]
        for j in range(n+(2*m)+2):
            if j < n+m+1:
                if i==0:
                    if j<n+1:
                        if j ==0:
                            auxTabla.append(1)
                        else:
                            auxTabla.append(Zopt[j-1])
                    else:
                         auxTabla.append(0)
                else:
                    auxTabla.append(Tabla[i][j])
        if i !=0 :            
            auxTabla.append(Tabla[i][n+(2*m)+1])
        else:
            auxTabla.append(0)
        AUXtabla.append(auxTabla)
    names_Image=Imprimir_Tabla(Tabla,n,m,faseDoble,H,Resultados,regPivote,names_Image)
    
    for i in range(n+1):
        aux=-AUXtabla[0][i]
        for j in range(n+m+2):
            if i!=0:
                AUXtabla[0][j]=AUXtabla[0][j]+(aux*AUXtabla[i][j])
            
        
    names_Image=Imprimir_Tabla(Tabla,n,m,faseDoble,H,Resultados,-1,names_Image)
    return Simplex(AUXtabla, n, m,faseDoble,names_Image)

#z=[2,3,5,2,7,2]
#A=[[-1,1,0,3,6,1],[1,2,11,5,0,1],[0,3,1,1,0,4],[0,4,5,0,1,7],[0,0,1,2,0,9],[9,3,2,0,10,12],[11,2,1,-2,1,10]]
#b=[1,11,18,1,20,1,10]
#h=[-1,-1,-1,-1,-1,-1,-1]
#n=6
#m=7
z=[1,4]
A=[[3,2],[4,5]]
b=[54,5]
h=[1,1]
n=2
m=2

#z=[2,7]
#A=[[1,2],[1,-1]]
#b=[2,1]
#h=[-1,-1]
#n=2
#m=2


a,b,c=inicializaSimplex(A,z,n,m,b,h,2)
print(a)
print(b)
print(c)
"""
A=Matriz de restricciones
z=vector de la fucion objetivo
n=numero de variables
m=numero de restricciones
b=vector de Desigualdades de las restricciones
h=vector igualdad desigualdad
1 si es maximizar y 2 si es minimizar
"""

        
        



