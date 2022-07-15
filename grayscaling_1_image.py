from PIL import Image
import numpy as np
import ctypes
import time
from os import scandir, getcwd

#SE USA ESTA FUNCION PARA OBTENER EL NOMBRE DE LOS ARCHIVOS DE UNA CARPETA
def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
 
#SE UTILIZARAN IMAGENES DE FORMATO JPEG POR UNA MAYOR RESOLUCION
#grayscl_asm = ctypes_function_asm()
if __name__ == '__main__':
    carpeta= ls("/content/FOTOS")
    print(carpeta)
    img = Image.open(r"/content/pulmon.jpeg")
    img_data = img.getdata()
    #aqui estan los datos de c
    #limite_c = xy * 3
    limite_c=len(img_data)
    #se genera un arreglo donde saldran los valores de resultado
    salida_c = np.zeros((limite_c,1),dtype=np.float32)
    #aqui se almacena un arreglo dentro de la codificacion en C
    entrada_c=np.array(img_data) 
    entrada_c=entrada_c.flatten()

    print(entrada_c)
    print(limite_c)

#######################################################################
            #EXCLUSIVO DE LENGUAJE C
#######################################################################

    # indicar la ruta de la shared library
    libfile = './GC_c.so'

    # cargar la shared library
    lib = ctypes.CDLL(libfile)

    # tipo de dato de los argumentos
    lib.GC.argtypes = [
        np.ctypeslib.ndpointer(dtype=np.float32),
        np.ctypeslib.ndpointer(dtype=np.float32),
        ctypes.c_int
        ]
    # funcion configurada

    funcion_c = lib.GC
    entrada_c=entrada_c.astype("float32")
    salida_c=salida_c.astype("float32")
    limite_c=int(limite_c)

    inicio_c = time.perf_counter()
    funcion_c(entrada_c,salida_c,limite_c)
    fin_c= time.perf_counter()

    salida_c=salida_c.round()
    salida_c=salida_c.astype(int)
    #print(entrada_c)
    #print(salida_c[0:100])
    
    lst=[]

  #######################################################################
              #EXCLUSIVO DE ENSAMBLADOR
  #######################################################################

    limite_asm=int(len(img_data))
    #se genera un arreglo donde saldran los valores de resultado
    salida_asm = np.zeros((limite_c,1),dtype=np.float32)
    #aqui se almacena un arreglo dentro de la codificacion en C
    entrada_asm=np.array(img_data,dtype=np.float32) 
    entrada_asm=entrada_asm.flatten()

    # indicar la ruta de la shared library
    libfiles = './grayscale_ASMO.so'

    # cargar la shared library
    libr = ctypes.CDLL(libfiles)

    # tipo de dato de los argumentos
    libr.GS_.argtypes = [
        np.ctypeslib.ndpointer(dtype=np.float32),
        np.ctypeslib.ndpointer(dtype=np.float32),
        ctypes.c_int
    ]

    
    funcion_asm = libr.GS_
    inicio_asm = time.perf_counter()
    funcion_asm(entrada_asm,salida_asm,limite_asm)
    fin_asm = time.perf_counter()
    salida_asm=salida_asm.round()
    salida_asm=salida_asm.astype(int)
    #print(entrada_asm)
    #print(salida_asm[0:1000])

    lst=[]


    #######################################################################
                #EXCLUSIVO DE PYTHON ITERATIVO
    #######################################################################
    inicio_py = time.perf_counter()
    for i in img_data:

        #lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114) ### Rec. 609-7 weights
        lst.append(i[0]*0.2125+i[1]*0.7174+i[2]*0.0721) ### Rec. 709-6 weights
    fin_py = time.perf_counter()
     #######################################################################
                #MUESTRA DE IMAGENES
    #######################################################################


    print(len(lst))
    new_img = Image.new("L", img.size)
    new_img.putdata(lst)
    new_img.save("SALIDA.jpg")
    new_img.show()

    new_img_c =Image.new("L", img.size)
    new_img_c.putdata(salida_c)
    new_img_c.save("SALIDA EN C.jpg")
    new_img_c.show()

    new_img_asm =Image.new("L", img.size)
    new_img_asm.putdata(salida_asm)
    new_img_asm.save("SALIDA EN ASM.jpg")
    new_img_asm.show()

    print(f"la funcion en python es de {fin_py-inicio_py} segundos")
    print(f"la funcion en c es de {fin_c-inicio_c} segundos")
    print(f"la funcion en asm es de {fin_asm-inicio_asm} segundos")
