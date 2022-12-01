
import cv2
import numpy as np


im=cv2.imread('C:/TESIS-DANIEL/Re-enfoque/ima1.png')
#cv2.imshow('imagen', im)
#IMPORTANTE SON 178 * 221 PIXELES

#img1=np.ones((178,221,3))  

#img1=img1*200
#vector=[]

img1=np.ones((3,5,3))
img1[0:1,0:5]= (0,255,0)
img1[1:2,0:5]= (0,0,255)
img1[2:3,0:5]= (255,0,0)

#1er imagen
#1er y 2do convinado
imx=im[0:40,0:7716]
cv2.imwrite('imx.png', imx)

#2do renglon fino
imx1=im[10:40,0:7716]
cv2.imwrite('imx1.png', imx1)
#3er renglon fino
imx2=im[40:70,0:7716]
cv2.imwrite('imx2.png', imx2)

#2do y 3ero fino
imxcov=im[10:70,0:7716]
cv2.imwrite('imxconv.png', imxcov)




#Puntos en y 2 renglones

imy=im[0:5364,0:35]
cv2.imwrite('imy.png', imy)

#puntos en y 1er renglon

imy1=im[0:5364,0:15]
cv2.imwrite('imy1.png', imy1)


#2do renglon

imy2=im[0:5364,15:35]
cv2.imwrite('imy2.png', imy2)



#se hallaron los centros para: imy2, imy1, imx1, imx2, a continuación se hace con imy2

#centros
gris=cv2.cvtColor(imy2, cv2.COLOR_BGR2GRAY)


#umbral threshold
ret,th=cv2.threshold(gris, 30, 255, cv2.THRESH_BINARY) #original estaba en 50

#contornos
contornos,jerarquia=cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE
cv2.drawContours(imy2, contornos, -1, (0,255,0),1)

centros=[]

for c in contornos:
    (x,y,w,h)=cv2.boundingRect(c)
    cv2.rectangle(imy2, (x,y), (x+w,y+h), (0,255,0),1)
    #print('El centro en x es=',x+(w/2),'el centro en y es=',y+(h/2))
    
    centros.append([int(y+(h/2)),int(x+(w/2))])  

print(centros)


    



















