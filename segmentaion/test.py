from imager import Imager
from kmeans import Kmeans
from mask import Mask

pixels, size= Imager.loadImagePixelsAndSize('a.jpg')
k = Kmeans(4, pixels, loops = 50)

Mask(k.clusters, pixels, size)