import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlib
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from kneed import KneeLocator
from mpl_toolkits.mplot3d import Axes3D

class ClusterPart:
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
    
    def elbow(self,listVar):
        SSE = []
        Matriz = np.array(self.dataDistances[listVar])
        PDM=pd.DataFrame(Matriz)
        #print(PDM)
        estandarizar=StandardScaler()
        MEstandarizada=estandarizar.fit_transform(Matriz)
        for i in range(2, 12):
            km = KMeans(n_clusters=i, random_state=0)
            km.fit(MEstandarizada)
            SSE.append(km.inertia_)
        kl = KneeLocator(range(2, 12), SSE, curve="convex", direction="decreasing")
        #print(kl.elbow)
        plt.style.use('ggplot')
        kl.plot_knee()
        plt.show()

    def Cent(self,variable,showText,listVar):
        SSE = []
        #print(listVar)
        Matriz = np.array(self.dataDistances[listVar])
        #PDM=pd.DataFrame(Matriz)
        #print(PDM)
        estandarizar=StandardScaler()
        MEstandarizada=estandarizar.fit_transform(Matriz) 
        #print(MEstandarizada)
        for i in range(2, 12):
            km = KMeans(n_clusters=i, random_state=0)
            km.fit(MEstandarizada)
            SSE.append(km.inertia_)
        kl = KneeLocator(range(2, 12), SSE, curve="convex", direction="decreasing")
        #print(kl.elbow)
        
        MParticional = KMeans(n_clusters=kl.elbow, random_state=0).fit(MEstandarizada)
        MParticional.predict(MEstandarizada)
        #print(MParticional.labels_)
        if(len(variable)!=0):
            self.dataDistances= self.dataDistances.drop(columns=[variable])
        self.dataDistances['clusterP'] = MParticional.labels_
        #print(self.dataDistances)
        Datainfo=list(self.dataDistances.groupby(['clusterP'])['clusterP'].count())
        #print(Datainfo)
        showText.clear()
        showText.append("Número de elementos de cada centroide:")
        for line in Datainfo:
            showText.append(str(line))
        CentroidesH = self.dataDistances.groupby(['clusterP'])[listVar].mean()
        CentroidesP = pd.DataFrame(CentroidesH)
        #print(CentroidesP)
        plt.rcParams['figure.figsize'] = (6, 5)
        plt.style.use('ggplot')
        catalogo=['red','m',"b","y","g","brown","k","grey","w","pink","c", "violet"]
        colores=[]
        for i in range(kl.elbow):
            colores.append(catalogo[i])
        #print(colores)
        asignar=[]
        for row in MParticional.labels_:
            asignar.append(colores[row])
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(MEstandarizada[:, 0], 
                MEstandarizada[:, 1], 
                MEstandarizada[:, 2], marker='o', c=asignar, s=60)
        ax.scatter(MParticional.cluster_centers_[:, 0], 
                MParticional.cluster_centers_[:, 1], 
                MParticional.cluster_centers_[:, 2], marker='o', c=colores, s=1000)
        plt.show()
        return CentroidesP