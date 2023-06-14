import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlib
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from sklearn.tree import plot_tree
from sklearn.tree import export_text

class ArbolC:
    def __init__(self,name):
        self.name = name
        self.DatosTransacciones = pd.read_csv(self.name)

    def MTemp(self):
        plt.figure(figsize=(12,6))
        MatrizInf = np.triu(self.DatosTransacciones.corr())
        sns.heatmap(self.DatosTransacciones.corr(), cmap='RdBu_r', annot=True, mask=MatrizInf)
        plt.show()
    
    def algoritmo(self,var,listVar,showText,showText2,a,b,c,num):
        #V predictoras
        X=np.array(self.DatosTransacciones[listVar])
        x=pd.DataFrame(X)
        #print(x)
        #V a pronosticar
        Y=np.array(self.DatosTransacciones[var])
        y=pd.DataFrame(Y)
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y,test_size=num, random_state=0, shuffle=True)
        #print(pd.DataFrame(X_train))
        #print(pd.DataFrame(Y_train))
        #Arbol
        if(a!=0&b!=0&c!=0):
            ClasificacionAD= DecisionTreeClassifier(max_depth=a, min_samples_split=b, min_samples_leaf=c)
        elif(a!=0&b!=0):
            ClasificacionAD= DecisionTreeClassifier(max_depth=a, min_samples_split=b)
        elif(a!=0&c!=0):
            ClasificacionAD= DecisionTreeClassifier(max_depth=a, min_samples_leaf=c)
        elif(b!=0&c!=0):
            ClasificacionAD= DecisionTreeClassifier(min_samples_split=b, min_samples_leaf=c)
        elif(a!=0):
            ClasificacionAD= DecisionTreeClassifier(max_depth=a)
        elif(b!=0):
            ClasificacionAD= DecisionTreeClassifier(min_samples_split=b)
        elif(c!=0):
            ClasificacionAD= DecisionTreeClassifier(min_samples_leaf=c)
        else:
            ClasificacionAD= DecisionTreeClassifier(random_state=0)
        
        ClasificacionAD.fit(X_train, Y_train)
        Y_Clasificacion = ClasificacionAD.predict(X_validation)
        #print(pd.DataFrame(Y_Clasificacion))
        Valores = pd.DataFrame(Y_validation, Y_Clasificacion)
        #print(Valores)

        Y_Clasificacion = ClasificacionAD.predict(X_validation)
        Matriz_Clasificacion = pd.crosstab(Y_validation.ravel(), Y_Clasificacion, rownames=['Real'],colnames=['Clasificación']) 
        #print(Matriz_Clasificacion)
        ##
        #print('Criterio: \n', ClasificacionAD.criterion)
        #print('Importancia variables: \n', ClasificacionAD.feature_importances_)
        #print("Exactitud", ClasificacionAD.score(X_validation, Y_validation))
        #print(classification_report(Y_validation, Y_Clasificacion))
        ##
        showText.clear()
        showText.append("Criterio: "+str(ClasificacionAD.criterion))
        showText.append('Importancia variables: \n'+str(ClasificacionAD.feature_importances_))
        showText.append("Exactitud: "+str(round(ClasificacionAD.score(X_validation, Y_validation),4)))
        showText.append(str(classification_report(Y_validation, Y_Clasificacion)))
        ##Niveles del arbol
        plt.figure(figsize=(9,7))
        plot_tree(ClasificacionAD, feature_names = listVar)
        plt.show()
        #
        Reporte = export_text(ClasificacionAD, feature_names = listVar)
        #print(Reporte)
        showText2.clear()
        showText2.append(str(Reporte))
        return Matriz_Clasificacion

    def algoritmoN(self,var,listVar,v1,v2,v3,v4,v5,v6,Diag):
        #V predictoras
        X=np.array(self.DatosTransacciones[listVar])
        x=pd.DataFrame(X)
        print(x)
        #V a pronosticar
        Y=np.array(self.DatosTransacciones[var])
        y=pd.DataFrame(Y)
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y,test_size=0.2, random_state=1234, shuffle=True)
        print(pd.DataFrame(X_train))
        print(pd.DataFrame(Y_train))
        #Arbol
        ClasificacionAD= DecisionTreeClassifier(random_state=0)
        ClasificacionAD.fit(X_train, Y_train)
        Y_Clasificacion = ClasificacionAD.predict(X_validation)
        #print(pd.DataFrame(Y_Clasificacion))
        PacienteID1 = pd.DataFrame({'Texture': [v1],'Area': [v2], 'Smoothness': [v3],  'Compactness': [v4], 'Symmetry': [v5], 'FractalDimension': [v6]})
        print(ClasificacionAD.predict(PacienteID1)[0])
        if (ClasificacionAD.predict(PacienteID1)[0]=='M'):
            Diagnostico="Tumor Maligno"
        else:
            Diagnostico="Tumor Benigno"
        Diag.clear()
        Diag.setText(Diagnostico)