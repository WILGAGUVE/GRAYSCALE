extern void GS_asm(float *color, float *salida, int limite);

void GC(float *color, float *salida, int limite)
{
    int j=0;
    for(int i=0;i<limite;i++)
    {
        salida[i]=color[j]*0.2125+color[j+1]*0.7174+color[j+2]*0.0721;
        j=j+3;
    }
}
//convertir en flatten 
