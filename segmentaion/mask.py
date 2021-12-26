from PIL import Image
import logging

class Mask():
    def __init__(self, clusters, pixels, imagesize):
        logging.basicConfig(level=logging.INFO)
        logging.basicConfig(level=logging.DEBUG)

        logging.info('Masks init...')
        self.clusters = self.clustersIntoSets(clusters)
        self.imagesize = imagesize
        self.pixels = pixels
        self.images = self.initImages(len(clusters), imagesize)
        self.buildMasks()
        self.closeImages()

    def clustersIntoSets(self, clustersLists):
        logging.info("turning cluster lists into sets...")
        clustersSets = []
        for clu in clustersLists:
            clustersSets.append(set(clu))
        return clustersSets

    def initImages(self, count, imagesize):
        images = []
        for _ in range(count):
            images.append(Image.new('RGB', imagesize))
        return images
    
    def closeImages(self):
        logging.info('cloising images...')
        for i, im in enumerate(self.images):
            im.save(f'{i}.jpg')
    
    def buildMasks(self):
        logging.info('building masks...')
        for idx, pixel in enumerate(self.pixels):
            clusteridx=self.getPixelsClusteridx(pixel)
            # logging.debug(f'idx conversion {idx}, {self.to2d(idx)}')
            co = self.to2d(idx)
            if co[0] < self.imagesize[0] and co[1] < self.imagesize[1]:
                self.images[clusteridx].putpixel(self.to2d(idx), pixel)
    
    def getPixelsClusteridx(self, pixel):
        for idx, cluster in enumerate(self.clusters):
            if pixel in cluster:
                return idx
        raise Exception(f'pixel doesnot belong to any cluster {pixel}') 


    def to2d(self, idx):
        return idx//self.imagesize[0], idx%self.imagesize[1]