from re import A
import cv2
from os import scandir, getcwd
import os
import errno
import time
from cv2 import rotate
import matplotlib.pyplot as plt
import numpy as np

OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
BOLD = '\033[1m'
YELLOW='\033[93m'

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def grayscale():
    carpeta= ls(r"C:\Users\WILSON\Desktop\GRAYSCALE\fotos")
    
    try:
        os.mkdir(r"C:\Users\WILSON\Desktop\GRAYSCALE\RESULTADO DE FOTOS FUNCIONAL")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    TIEMPOS=[]
    index=[]
    ARMONICAS=[]
    for i in carpeta:
        ########## CONVERSION DE IMAGEN ##########
        inicio=time.perf_counter()
        image = cv2.imread(r'C:\Users\WILSON\Desktop\GRAYSCALE\fotos\%s' %str(i))
        for j in range(10):
            #print(image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #print(i)
            #cv2.imshow('Original image RADIO',image)
            cv2.imwrite(f"./RESULTADO DE FOTOS FUNCIONAL/SALIDA en PYTHON de {str(i)}.png", gray)
        fin=time.perf_counter()
        ########## MEDICION DE TIEMPOS  PROMEDIOS ##########
        TIEMPOS.append((fin-inicio)/10)
        PRE_ARMONICA = np.array(TIEMPOS)
        ARMONICA=1/np.mean(1/PRE_ARMONICA)
        ARMONICAS.append(ARMONICA)
        
        ########## IMPRESION AL TERMINAL ##########
        print(OKGREEN+f"el tamano de {str(i)} es: ",gray.shape)
        print(OKCYAN+f"Tiempo de ejecucion medio de {str(i)}: {(fin-inicio)/10}")
        print(YELLOW+f"Tiempo de ejecucion armonico de {str(i)}: {ARMONICA}")
        index.append(str(gray.shape))
        
    ########## EXPORTACION A CSV ##########    
    with open('tiempos_funcional.csv', 'a', encoding='UTF8') as f:
        f.write(f"ARCHIVO,ANCHO, ALTO,TIEMPO MEDIO,TIEMPO M ARMONICO\n")
        for i in range(len(TIEMPOS)):
            f.write(f"{carpeta[i]},{index[i]},{TIEMPOS[i]},{ARMONICAS[i]}\n")
    
    ########## GRAFICA DE TIEMPOS ##########
    plt.xlabel('tamagno')
    plt.xticks(rotation=90)
    plt.ylabel('tiempo')
    plt.title(f"TIEMPOS DE PYTHON FUNCIONALMENTE",fontdict={'color' : 'darkblue','size': '18'})
    plt.plot(index, TIEMPOS, 'g-o', label="media")
    plt.plot(index, ARMONICAS, 'b-o', label="armonica")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"./PROCESOS Y RESULTADO DE FUNCIONAL TIEMPO.png")
    #print("el tiempo de la carpreta", carpeta, "es" , TIEMPOS )


if __name__ == '__main__':
    with open('tiempos_funcional.csv', 'w', encoding='UTF8') as f:
        f.close()
    inicio_py_fun = time.perf_counter()
    grayscale()
    fin_py_fun = time.perf_counter()
    print(OKBLUE+BOLD+"el tiempo de ejecucion medio es:" ,(fin_py_fun-inicio_py_fun)/10, " segundos")