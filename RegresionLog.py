import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlib
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

class RLogistica:
    def __init__(self,name):
        self.name = name
        self.DatosTransacciones = pd.read_csv(self.name)

    def infoD(self,Qtext):
        Qtext.clear()
        information=self.DatosTransacciones.dtypes
        #print(information)
        Qtext.append(str(information))
    
    def evalVisual(self,var):
        if(len(var)!=0):
            sns.pairplot(self.DatosTransacciones, hue=var)
            plt.show()
        else:
            sns.pairplot(self.DatosTransacciones)
            plt.show()
    
    def MCorrelaciones(self):
        CorrM = self.DatosTransacciones.corr(method='pearson')
        PCM=pd.DataFrame(CorrM)
        #print(PCM)
        plt.figure(figsize=(12,5))
        MatrizInf = np.triu(CorrM)
        sns.heatmap(CorrM, cmap='RdBu_r', annot=True, mask=MatrizInf)
        plt.show()
        return PCM
    
    def algoritmo(self,var,listVar,num,showText):
        #print(listVar)
        #print(var)
        try:
            int(self.DatosTransacciones[var][0])
            float(self.DatosTransacciones[var][0])
        except Exception:
            #print("Nop, no se puede convertir a numero")
            a=self.DatosTransacciones[var][0]
            for i in self.DatosTransacciones[var]:
                if(i!=a):
                    b=i
            #print('valor de a',a)
            #print('valor de b',b)
            self.DatosTransacciones = self.DatosTransacciones.replace({a: 0, b: 1})
            #print(self.DatosTransacciones)
        #else:
            #print("Sí se pudo convertir a numero")
            
        #V predictoras
        X = np.array(self.DatosTransacciones[listVar])
        x=pd.DataFrame(X)
        print(x)
        #V de clase
        Y = np.array(self.DatosTransacciones[var])
        y=pd.DataFrame(Y)
        print (y)
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y,test_size = num,random_state = 1234, shuffle = True)
        #print(pd.DataFrame(X_train))
        #print(pd.DataFrame(Y_train))
        Clasificacion = linear_model.LogisticRegression()
        Clasificacion.fit(X_train, Y_train)
        Probabilidad = Clasificacion.predict_proba(X_validation)
        #print(pd.DataFrame(Probabilidad))
        Predicciones = Clasificacion.predict(X_validation)
        #print(pd.DataFrame(Predicciones))
        Y_Clasificacion = Clasificacion.predict(X_validation)
        Matriz_Clasificacion = pd.crosstab(Y_validation.ravel(), Y_Clasificacion, rownames=['Real'],colnames=['Clasificación']) 
        MC=pd.DataFrame(Matriz_Clasificacion)
        #print(MC)
        ##
        showText.clear()
        showText.append("Exactitud: "+str(round(Clasificacion.score(X_validation, Y_validation),4)))
        showText.append('\nProb = 1/1+𝑒^−(𝑎+𝑏𝑋))')
        showText.append('𝑎+𝑏𝑋 =('+str(round(float(Clasificacion.intercept_),4))+')')
        for i in range(len(listVar)):
            showText.append('+('+str(round(float(Clasificacion.coef_[0][i]),4))+')*'+listVar[i])
        showText.append(str(classification_report(Y_validation, Y_Clasificacion)))
        ##
        #print("Exactitud", Clasificacion.score(X_validation, Y_validation))
        #print(classification_report(Y_validation, Y_Clasificacion))
        #print("Intercept:", Clasificacion.intercept_)
        #print('Coeficientes: \n', Clasificacion.coef_)
        #print('Prob = 1/1+𝑒^−(𝑎+𝑏𝑋))')
        #print('𝑎+𝑏𝑋 =(',Clasificacion.intercept_+') + (',listVar[0]+')'+Clasificacion.coef_[0][0])
        ##
        return MC