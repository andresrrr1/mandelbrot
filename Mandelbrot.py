import numpy as np #se importa la libreria numpy y se le asigna un apodo para agilizar el programa
import matplotlib.pyplot as plt # se importa otra libreria en la cual contiene diferentes variables a la de numpy como 
#plt.figure(): Crea una nueva figura.
# plt.subplot(): Crea un subplot dentro de una figura.
# plt.clf(): Borra la figura actual.
# plt.close(): Cierra la figura actual.
# plt.show(): Muestra la figura actual.
def mandelbrot(h, w, maxit=20, r=2): # se define una varible la cual se encunetra en matplotlib.pyplot, la cual tiene 4 parametros 
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    
        div_now = diverge & (divtime == maxit)  
        divtime[div_now] = i                    
        z[diverge] = r                          

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))