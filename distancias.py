import PyQt5
import pandas as pd     #Manipular datos 
import numpy as np      #Vectores y matrices
import matplotlib.pyplot as plt   #Gráficas
from scipy.spatial.distance import cdist #Calculo de distancias
from scipy.spatial import distance #Calculo de distancias
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class Distances:
    def __init__(self,name):
        self.name = name
        self.dataDistances = pd.read_csv(self.name)
    
    def MatrizEclideana(self):
        DstEuclidiana=cdist(self.dataDistances,self.dataDistances,metric='euclidean')
        MEuclidiana=pd.DataFrame(DstEuclidiana)
        #print(MEuclidiana)
        return MEuclidiana

    def MatrizChebyshev(self):
        #print(self.dataDistances)
        DstCheb=cdist(self.dataDistances,self.dataDistances,metric='chebyshev')
        MCheb=pd.DataFrame(DstCheb)
        #print(MCheb)
        return MCheb

    def MatrizManhattan(self):
        #print(self.dataDistances)
        DManhattan=cdist(self.dataDistances,self.dataDistances,metric='cityblock')
        MManhattan=pd.DataFrame(DManhattan)
        #print(MManhattan)
        return MManhattan
    
    def MatrizMinkowski(self):
        #print(self.dataDistances)
        DMin=cdist(self.dataDistances,self.dataDistances,metric='minkowski',p=1.5)
        MMin=pd.DataFrame(DMin)
        #print(MManhattan)
        return MMin