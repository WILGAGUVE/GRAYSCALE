
from PIL import Image
import numpy as np
import ctypes
import time
import os
import errno
from os import scandir, getcwd
import multiprocessing as mp 
from multiprocessing import Pool, cpu_count, current_process
num_proc=4
TIEMPOS=[]
import cv2
import statistics
import matplotlib.pyplot as plt
import time

OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
BOLD = '\033[1m'

def filtro_mediana(sign, ventana):
    signc = []
    tam = len(sign)
    offs = int((ventana-1)/2)
    for i in range(tam):
        inicio = i - offs if (i - offs > 0) else i
        fin = i + offs if (i + offs < tam) else tam
        signc.append(statistics.median(sign[inicio:fin]))
    return signc

#SE USA ESTA FUNCION PARA OBTENER EL NOMBRE DE LOS ARCHIVOS DE UNA CARPETA
def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
  


#SE UTILIZARAN IMAGENES DE FORMATO JPEG POR UNA MAYOR RESOLUCION
#grayscl_asm = ctypes_function_asm()
def grayscale(*carpeta):
    #LA CARPTETA DONDE SE EXTRAEN LAS IMAGENES PUEDE SER MODIFICABLE
    for _ in range(len(carpeta)):
        try:
            os.mkdir('RESULTADO DE FOTOS')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        
        #######################################################################
                    #EXCLUSIVO DE PYTHON FUNCIONAL
        #######################################################################
        imagen_prueba = cv2.imread(r"C:\Users\WILSON\Desktop\GRAYSCALE\fotos\%s" %str(carpeta[_]))
        #print(imagen_prueba)
        inicio_py_fun = time.perf_counter()
        for m in range(10):
            gray = cv2.cvtColor(imagen_prueba, cv2.COLOR_BGR2GRAY)
        fin_py_fun = time.perf_counter()
        cv2.imwrite(f"./RESULTADO DE FOTOS/SALIDA en PYTHON de {str(carpeta[_])}", gray);
        
        TIEMPOS.append((fin_py_fun-inicio_py_fun)/10)
    p=current_process()
    with open('tiempos.csv', 'a', encoding='UTF8') as f:
        
        f.write(f"proceso {p._identity[0]},{str(sum(TIEMPOS))}\n")
    p=current_process()
    index = carpeta
    #index = range(len(TIEMPOS))
    plt.bar( index, TIEMPOS, color='b')
    plt.xlabel('tamagno')
    plt.ylabel('tiempo')
    plt.title(f"TIEMPOS DE PYTHON EN EL PROCESO {p._identity[0]}",fontdict={'color' : 'darkblue','size': 10})
    #plt.plot(index, TIEMPOS, 'r-o', label=f"python en {str(carpeta)}")
    #plt.legend()
    plt.tight_layout()
    plt.savefig(f"{num_proc} PROCESOS Y RESULTADO DE {p._identity[0]} PROCESO.png")
    print(OKGREEN+"el tiempo en el proceso ", p._identity[0], "es" , TIEMPOS )
    print(OKBLUE+"el tiempo Total en el proceso ", p._identity[0], "es" , sum(TIEMPOS) )
    
items=[]
if __name__ == '__main__':
    #grayscale()
    carpeta= ls(r"C:\Users\WILSON\Desktop\GRAYSCALE\fotos")
    print(carpeta)
    
    with open('tiempos.csv', 'w', encoding='UTF8') as f:
        f.close()
    
    inputs =[carpeta[int(len(carpeta)*i/num_proc):int(len(carpeta)*(i+1)/num_proc)] for i in range(num_proc)]
    print(inputs)
    pool = Pool(processes = 4)
    INICIIO=time.perf_counter()
    pool.starmap(func=grayscale, iterable=inputs)
    FINN=time.perf_counter()
    print(BOLD+OKCYAN+"el tiempo total de ejecucuion paralela es", (FINN-INICIIO)/10)
    pool.close()
    
    
    
    