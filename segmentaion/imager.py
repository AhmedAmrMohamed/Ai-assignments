from PIL import Image

class Imager:
    ''' handles the all the related image loading and saving stuff.'''

    def loadImagePixelsAndSize(path):
        image = Image.open(path)
        pixels = []
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixels.append(image.getpixel((x, y)))
        assert len(pixels) == image.size[0]*image.size[1], "len pixels is wrong."
        return pixels, image.size

    def saveImagePixels(pixels, path, size):
        image = Image.new('RGB', size)
        idx = 0
        for x in range(size[0]):
            for y in range(size[1]):
                if(len(pixels)==idx):
                    save(image, path)
                    return
                image.putpixel((x, y), pixels[idx])
                idx+=1
        Imager.save(image, path)
        
    def save(image, path):
        image.save(path)

'''test'''

# pi= Imager.loadImagePixels('a.jpg')
# Imager.saveImagePixels(pi, 'b.jpg', (224, 225))