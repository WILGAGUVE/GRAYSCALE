import csv
import numpy as np
import matplotlib.pyplot as plt
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
BOLD = '\033[1m'
temp=[]
item1=[]
item2=[]

if __name__ == '__main__':
    with open('tiempos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            item1.append(float(row[1]))
    print(OKBLUE+ "Tiempo Funcional")
    print(item1)    
    
    with open('tiempos1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            item2.append(float(row[1]))
    print(OKGREEN+ "Tiempo Iterativo")
    print(item2)
    index = ["PROCESO 1", "PROCESO 2", "PROCESO 3", "PROCESO 4"]
    x_axis = np.arange(len(index))
    plt.bar( x_axis -0.2, item1, color='r',width=0.4, label='FUNCIONAL' ) #AQUI VA EL CODIGO EN FUNCIONAL
    plt.bar( x_axis +0.2, item2, color='c',width=0.4, label='ITERATIVO') #AQUI VA EL CODIGO EN ITERATIVO
    
    plt.xticks(x_axis, index)
    plt.xlabel('GRUPOS')
    plt.ylabel('tiempo')
    plt.title(f"TIEMPOS DE PYTHON EN MULTIPROCESING FUNCIONAL",fontdict={'color' : 'darkblue','size': 10})
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"PROCESOS Y RESULTADO DE ITERATIVO TIEMPO.png")
    
    