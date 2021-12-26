import random
from math import inf, sqrt
import logging

class Kmeans():

    def __init__(self, k, pixels, loops = 10, randomSeed=None):
        # logging.basicConfig(level=logging.DEBUG)
        # logging.basicConfig(level=logging.INFO)
        self.k = k
        self.pixels = pixels
        self.loops = loops
        self.randomSeed = randomSeed
        self.centers =  self.initCenters()
        # self.centers =  [(255, 255, 255), (255, 0, 0), (0, 255, 0)]
        self.clusters = [_ for _ in self.centers]
        self.core()

    def core(self):
        # 1.get mean centers
        # 2.get variance, if variance > val: end ops
        # 3.assign pixels to clusters
        # goto 1
        logging.info("star core")
        logging.debug(f"\n\tclusters {self.clusters}\n\tcenters {self.centers}")
        while self.loops > 0:
            self.loops-=1
            logging.info(f'loops {self.loops}')
            self.clusters = self.assignToClusters()
            logging.info(f'clusters assigned')
            self.centers = self.getNewCenters()
            logging.info(self.clusterVariance(self.clusters[0]))


    def initCenters(self):
        centers = []
        for rc in self.randomCenters():
            centers.append( rc)
        return centers
    
    def randomCenters(self):
        if self.randomSeed != None:
            random.seed(self.randomSeed)
        rc = tuple(random.choices(self.pixels, k=self.k))
        logging.debug(f'random centers: {rc}')
        return rc
    
    def getNewCenters(self):
        centers = []
        # for i, cluster in enumerate(self.clusters):
        #     logging.info(f'cluster {i} len {len(cluster)}')
        for cluster in self.clusters:
            centers.append(self.clusterMean(cluster))
        return centers

    def clusterVariance(self, cluster):
        if(len(cluster) < 1):
            return (inf, inf, inf)
        negmean = self.pixelDiv(self.clusterMean(cluster), -1) # mean*=-1
        su = (0, 0, 0)
        for pix in cluster:
            t = self.pixelToPower(self.pixelSum(pix, negmean), 2)
            su = self.pixelSum(t, su)
        su = self.pixelDiv(su, len(cluster)-1)
        return su

    def clusterMean(self, cluster):
        # logging.debug(f'cluster mean:\n\tcluster : {cluster}, {len(cluster)}')
        su = [0, 0, 0]
        # if(len(cluster) == 0):
        #     return (0, 0, 0)
        for pi in cluster:
            for i in (0, 1, 2):
                su[i] += pi[i]**2
        for idx,val in enumerate(su):
            su[idx] = int(sqrt(val/ len(cluster)))
        return tuple(su)
    
    def assignToClusters(self):
        _greens = 0
        clusters = [[] for _ in range(self.k)]
        for px in self.pixels:
            idx = self.closestCenterToPixel(px)
            clusters[idx].append(px)
        return clusters
    
    def closestCenterToPixel(self, pixel):
        closestcenter = 0
        mindis = inf
        for idx, c in enumerate(self.centers):
            dis = self.pixelsDistance(c, pixel)
            # logging.debug(f"center {c} pixel {pixel} distance {dis}")
            if dis < mindis:
                mindis = dis
                closestcenter = idx
        return closestcenter

    def pixelsDistance(self, A, B):
        assert(type(A) == type(())), f'============ {type(A)} {A}'
        assert(type(B) == type(())), f'============ {type(B)} {B}'
        su = 0
        for i in (0, 1, 2):
            su += (A[i]-B[i])**2
        return su**0.5

    def pixelSum(self, A, B):
        '''A+B'''
        su = [0, 0, 0]
        for i in (0, 1, 2):
            su[i] = A[i]+B[i]
        return tuple(su)

    def pixelDiv(self, A, B):
        ''' A/B , A: tuple, B: int'''
        su = [0, 0, 0]
        for i in (0, 1, 2):
            su[i] = A[i]//B
        return tuple(su) 

    def pixelToPower(self, A, B):    
        ''' A**B'''
        su = [0, 0, 0]
        for i in (0, 1, 2):
            su[i] = A[i]**B
        return tuple(su)