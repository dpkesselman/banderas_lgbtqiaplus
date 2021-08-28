# Primer paso:
# Instalar librerías: Numpy, OpenCV (pronto agregaré cómo instalarlas, por si no saben)
# Importar librerías.

import numpy as np
import cv2

# Empezamos a construir la imagen

img1 = np.zeros((600, 800, 3), np.uint8)
# "img1" es la variable en la que se va a guardar nuestra imagen en el código. Puede tener cualquier otro nombre
# que deseen en vez de "img1".

# "np.zeros" nos crea el fondo de la imagen, de color negro. "np.ones" nos crea una imagen de fondo negro pero 1 valor
# más alto en la escala de grises. Esto quiere decir que el fondo negro pleno se crea con "np.zeros", y "np.ones" nos
# sirve para subir en la escala de grises a través de la multiplicación. Si pusiésemos 200*np.ones nos crearía una
# imagen de fondo claro tirando a blanco.

# Los parámetros (aquello que va entre paréntesis) de np.zeros están conformados por las medidas de la imagen en px y
# su cantidad de canales (acá usamos 3 canales, red, green y blue, pero bien puede ser 1 y que la imagen resulten en una
# escala de grises).
# Es decir que la fórmula sería así: np.zeros((ancho, alto, cantidad de canales)

# "uint8" es el tipo de dato que va a procesar Python. En este caso, imágenes de 8 bits. Si queremos que sea de 16,
# tenemos que poner "uint16" y multiplicar por 256 este fragmento: (600, 800, 3), np.uint16). O sea, quedaría así:
# (600, 800, 3), np.uint16)*256.
# Si quisiéramos que fuese npuint32, debemos dividir en vez de multiplicar: (600, 800, 3), np.uint16)/256


# A continuación, la imagen se desarma en listas que contienen pixeles:
# img1[primer elemento : ultimo elemento (del ancho a cubrir),
#      primer elemento:ultimo elemento (del alto a cubrir)] = numero del color en BGR
# Los elementos corresponden a medidas en pixeles, por lo tanto 151:300 significa que va desde el pixel 151 al pixel 300
# Si el elemento contiene sólo un número anterior a ":", significa que cubrimos todo a partir de ese pixel.
# Si el elemento contiene sólo un número posterior a ":", significa que cubrimos todo antes de ese pixel.
# (no sé por qué me resaltó esa parte del texto, no fue intencional)
# Si el elemento sólo tiene ":", significa que estamos cubriendo el total de pixeles de ese ancho o alto.

# Cada línea corresponde a una franja de color. Podemos chequear los colores acá: https://www.cdmon.com/es/tabla-colores
# Cuando pasemos el RGB (RED, GREEN, BLUE) al código tenemos que hacerlo en este orden: BLUE, GREEN, RED.

# BANDERA PRIDE
img1[:100, :] = (0, 0, 255) # rojo
img1[100:200, :] = (0, 165, 255) # naranja
img1[201:300, :] = (0, 255, 255) # amarillo
img1[301:400, :] = (0, 128, 0) # verde
img1[401:500, :] = (255, 0, 0) # azul
img1[501:, :] = (128, 0, 128) # violeta

# BANDERA ASEXUAL
# img1[:150, :] = (0, 0, 0) #negro
# img1[151:300, :] = (128, 128, 128) #gris
# img1[301:450, :] = (255, 255, 255) #blanco
# img1[451:, :] = (128, 0, 128) #violeta

# Finalmente, guardamos la imagen creada en un archivo. Ojo, si vamos a hacer varias, siempre cambiar el nombre para
# no sobreescribirla. En este caso, el nombre es "Bandera_Pride.jpg". Siempre ponemos el formato de la imagen para que
# sepa en qué formato guardarlo.
cv2.imwrite('Bandera_Pride.jpg', img1)

# Para información más detallada a nivel Python pueden revisar este enlace, que fue el que yo usé para crear esto:
# https://noemioocc.github.io/posts/Crear-una-imagen-BGR-openCV-Python/
