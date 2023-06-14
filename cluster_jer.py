from numpy.core.fromnumeric import var
import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlib
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, MinMaxScaler
#%matplotlib inline 


class ClusterJer:
    def __init__(self,name):
        self.name = name
        self.dataDistances = pd.read_csv(self.name)

    def infoD(self,Qtext):
        information=self.dataDistances.dtypes
        #print(information)
        Qtext.clear()
        Qtext.append(str(information))
    
    def evalVisual(self,var):
        if(len(var)!=0):
            sns.pairplot(self.dataDistances, hue=var)
            plt.show()
        else:
            sns.pairplot(self.dataDistances)
            plt.show()
    
    def MCorrelaciones(self):
        CorrM = self.dataDistances.corr(method='pearson')
        PCM=pd.DataFrame(CorrM)
        plt.figure(figsize=(12,5))
        MatrizInf = np.triu(CorrM)
        sns.heatmap(CorrM, cmap='RdBu_r', annot=True, mask=MatrizInf)
        plt.show()
        return PCM

    def arbol(self,listVar,x,y,nc):
        Matriz = np.array(self.dataDistances[listVar])
        PDM=pd.DataFrame(Matriz)
        #print(PDM)
        estandarizar=StandardScaler()
        MEstandarizada=estandarizar.fit_transform(Matriz) 
        PDME=pd.DataFrame(MEstandarizada)
        #print(PDME)
        plt.figure(figsize=(10, 7))
        plt.title("Árbol de clusters")
        plt.xlabel(x)
        plt.ylabel(y)
        Arbol = shc.dendrogram(shc.linkage(MEstandarizada, method='complete', metric='euclidean'))
        if(nc!=0):
            plt.axhline(y=nc, color='purple', linestyle='--')
        plt.show()

    def Cent(self,nc,variable,showText,listVar):
        #print('Variables:')
        #print(listVar)
        Matriz = np.array(self.dataDistances[listVar])
        estandarizar=StandardScaler()
        MEstandarizada=estandarizar.fit_transform(Matriz)
        MJerarquico = AgglomerativeClustering(n_clusters=nc, linkage='complete', affinity='euclidean')
        MJerarquico.fit_predict(MEstandarizada)
        #print(MJerarquico.labels_)
        if(len(variable)!=0):
            self.dataDistances= self.dataDistances.drop(columns=[variable])
        self.dataDistances['clusterH'] = MJerarquico.labels_
        #print(self.dataDistances)
        Datainfo=list(self.dataDistances.groupby(['clusterH'])['clusterH'].count())
        #print(Datainfo)
        showText.clear()
        showText.append("Número de elementos de cada centroide:")
        for line in Datainfo:
            showText.append(str(line))
        CentroidesH = self.dataDistances.groupby(['clusterH'])[listVar].mean()
        CentroidesF = pd.DataFrame(CentroidesH)
        #print(CentroidesF)
        plt.figure(figsize=(8, 5))
        plt.scatter(MEstandarizada[:,0], MEstandarizada[:,1], c=MJerarquico.labels_)
        plt.grid()
        plt.show()
        return CentroidesF