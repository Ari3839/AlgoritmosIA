import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlib
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

class RLogisticaN:
    def __init__(self,name):
        self.name = name
        self.DatosTransacciones = pd.read_csv(self.name)

    def algoritmoN(self,var,listVar,num,Diag,valores):
        try:
            int(self.DatosTransacciones[var][0])
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
        #print(x)
        #V de clase
        Y = np.array(self.DatosTransacciones[var])
        y=pd.DataFrame(Y)
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
        #print("Exactitud", Clasificacion.score(X_validation, Y_validation))
        #print(classification_report(Y_validation, Y_Clasificacion))
        #print("Intercept:", Clasificacion.intercept_)
        #print('Coeficientes: \n', Clasificacion.coef_)
        #print('Prob = 1/1+𝑒^−(𝑎+𝑏𝑋))')
        PacienteID1 = pd.DataFrame({'Texture': [valores[0]], 'Area': [valores[1]], 'Smoothness': [valores[2]], 'Compactness': [valores[3]], 'Symmetry': [valores[4]], 'FractalDimension': [valores[5]]})
        Diagnostico=""
        if (Clasificacion.predict(PacienteID1)[0]==0):
            Diagnostico="Tumor Maligno"
        else:
            Diagnostico="Tumor Benigno"
        Diag.clear()
        Diag.setText(Diagnostico)
        #print('Diagnostico final:'+str(Clasificacion.predict(PacienteID1)[0])+Diagnostico)
