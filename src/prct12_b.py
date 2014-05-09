#!/src/bin/python

import modulo
import time
import matplotlib.pylab as pl


nro_test=10
intervalos=[10, 50, 100, 150, 500, 550, 1000]
umbral=[1e-3, 1e-4, 1e-5, 1e-6, 1e-7]


p=[]
for n in intervalos:
  ci=time.clock()
  e=modulo.error(n, nro_test, 1e-4)
  cf=time.clock() 
  tp=cf-ci
  p=p+[tp] 
 

pl.figure(figsize=(10,10), dpi=80)
pl.subplot(2,1,1)
pl.plot(intervalos,p, color="red", linewidth=2.5, linestyle="-")
pl.xticks([10, 50, 100, 150, 500, 1000])
pl.title(r'Tiempo')
pl.xlabel('Intervalos')
pl.ylabel('Tiempo en segundos')
pl.xlim(-10, 1100)
pl.ylim(-0.001, 0.14)
pl.savefig("prct13.eps", dpi=72)
pl.show()

a=[]
for i in intervalos:
  porcentaje=[]
  for a in umbral:
    x=modulo.error(n, nro_test, umbral)
    porcentaje = porcentaje + [x]
  a = a + [p]

pl.subplot(2,1,1)
pl.plot(umbral, color="blue", linewidth=2.5, linestyle="-", label=10)
pl.plot(umbral, color="red", linewidth=2.5, linestyle="-", label=50)
pl.plot(umbral, color="green", linewidth=2.5, linestyle="-", label=100)
pl.title(r'Porcentaje de fallos') 
pl.xlabel('Umbral')
pl.ylabel('Tiempo en segundos')

