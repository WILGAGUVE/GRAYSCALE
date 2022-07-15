
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
import csv
import matplotlib.pyplot as plt
import time


OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
BOLD = '\033[1m'


#SE USA ESTA FUNCION PARA OBTENER EL NOMBRE DE LOS ARCHIVOS DE UNA CARPETA
def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
  



#SE UTILIZARAN IMAGENES DE FORMATO JPEG POR UNA MAYOR RESOLUCION
#grayscl_asm = ctypes_function_asm()
def grayscale(*carpeta):
    
    #LA CARPTETA DONDE SE EXTRAEN LAS IMAGENES PUEDE SER MODIFICABLE
    for _ in range(len(carpeta)):
      inicio_py_fun = time.perf_counter()
      img = Image.open(r"C:\Users\WILSON\Desktop\GRAYSCALE\fotos\%s" %str(carpeta[_]))
      img_data = img.getdata()

      try:
          os.mkdir('RESULTADO DE FOTOS')
      except OSError as e:
          if e.errno != errno.EEXIST:
              raise
      
      
      #######################################################################
                  #EXCLUSIVO DE PYTHON ITERATIVO
      #######################################################################
      inicio_py = time.perf_counter()
      for n in range(10):
        lst=[]
        for m in img_data:
            try:
                lst.append(((m[0]*0.2125+m[1]*0.7174+m[2]*0.0721))) 
            except:
                pass
      
      fin_py = time.perf_counter()
      new_img = Image.new("L", img_data.size)
      new_img.putdata(lst)
      new_img.save(f"./RESULTADO DE FOTOS/SALIDA en PYTHON ITERATIVO de {str(carpeta[_])}")
      #######################################################################

      TIEMPOS.append((fin_py-inicio_py)/10)
    p=current_process()
    with open('tiempos1.csv', 'a', encoding='UTF8') as f:
        f.write(f"proceso {p._identity[0]},{str(sum(TIEMPOS))}\n")
    index = carpeta
    plt.bar( index, TIEMPOS, color='g')
    plt.xlabel('tamagno')
    plt.ylabel('tiempo')
    plt.title(f"TIEMPOS DE PYTHON EN {str(carpeta)}",fontdict={'color' : 'darkblue','size': 10})
    #plt.plot(index, TIEMPOS, 'g-o', label=f"python en {str(carpeta)}")
    #plt.legend()
    plt.tight_layout()
    plt.savefig(f"{num_proc} RESULTADO ITERATIVO DE DEL PROCESO {p._identity[0]}.png")
    print(OKGREEN+"el tiempo del proceso ", p._identity[0] ,"es" , TIEMPOS )
    print(OKBLUE+"el tiempo Total del proceso ", p._identity[0], "es" , sum(TIEMPOS) )
    

if __name__ == '__main__':
    #grayscale()
    carpeta= ls(r"C:\Users\WILSON\Desktop\GRAYSCALE\fotos")
    print(carpeta)
    
    with open('tiempos1.csv', 'w', encoding='UTF8') as f:
        f.close()
    
    inputs =[carpeta[int(len(carpeta)*i/num_proc):int(len(carpeta)*(i+1)/num_proc)] for i in range(num_proc)]
    print(inputs)
    pool = Pool(processes = cpu_count())
    INICIIO=time.perf_counter()
    pool.starmap(func=grayscale, iterable=inputs)
    FINN=time.perf_counter()
    print(BOLD+OKCYAN+"el tiempo total de ejecucion paralela es", (FINN-INICIIO)/10)
    pool.close()
    
    