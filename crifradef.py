# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:54:37 2021

@author: dox94
"""

def elimtilde(linea):
    nlinea = linea
    nlinea = nlinea.replace('á','a')
    nlinea = nlinea.replace('é','e')
    nlinea = nlinea.replace('í','i')
    nlinea = nlinea.replace('ó','o')
    nlinea = nlinea.replace('ú','u')
    return nlinea
    
def mayusculas(linea):
    nlinea = linea
    nlinea = nlinea.upper()
    return nlinea

def espacios(linea):
    nlinea = linea
    nlinea = nlinea.replace(' ','')
    return nlinea

def numerar(clave1,clave2):
    
    a=[0]*len(clave1)
    for i in range(len(clave1)):
        for j in range(len(clave1)):
            if(clave1[i] == clave2[j] and a[i] == 0):
                if(j+1 in a):
                    continue
                
                a[i] = j+1
                break
    return a

def encriptar(mensaje,clave):
    mensajeEnc = mensaje
    claveEnc = clave
    mensajeEnc = elimtilde(mensajeEnc)
    mensajeEnc = mayusculas(mensajeEnc)
    mensajeEnc = espacios(mensajeEnc)
    claveEnc = claveEnc.upper()
    clave_sep = list(claveEnc)
    clave_sep2 = clave_sep[:]
    clave_sep2.sort()
    clave_int = numerar(clave_sep,clave_sep2)
    
    cripto = [[0 for col in range(len(clave_sep))] for row in range(len(clave_sep))]
    
    cant = 1
    cant_men = 0
    for i in range(len(clave_sep)):
        if(cant_men == len(mensajeEnc)):
            break
        for j in range(len(clave_sep)):
            if(cant_men == len(mensajeEnc)):
                break
        
            elif(clave_int[j] == cant):
                cripto[i][j] = mensajeEnc[cant_men]
                cant_men = cant_men+1
                cant = cant+1
            
                break
            cripto[i][j] = mensajeEnc[cant_men]
            cant_men = cant_men +1
    m=""
    for i in range(1,len(cripto)+1):
        k = clave_int.index(i)
        for j in range(len(cripto)):
            if(cripto[j][k] == 0):
                continue
            m = m + cripto[j][k]
    
        m = m+" "
    return m
    
    

print("Mensaje")
mensaje = input()
print("Clave")
clave = input()
print(encriptar(mensaje, clave))





