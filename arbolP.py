import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlib
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn import model_selection
from sklearn.tree import export_graphviz
from sklearn.tree import plot_tree
from sklearn.tree import export_text

class ArbolP:
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
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y,test_size=num, random_state=1234, shuffle=True)
        #print(pd.DataFrame(X_train))
        #print(pd.DataFrame(Y_train))
        #Arbol
        if(a!=0&b!=0&c!=0):
            PronosticoAD = DecisionTreeRegressor(max_depth=a, min_samples_split=b, min_samples_leaf=c)
        elif(a!=0&b!=0):
            PronosticoAD = DecisionTreeRegressor(max_depth=a, min_samples_split=b)
        elif(a!=0&c!=0):
            PronosticoAD = DecisionTreeRegressor(max_depth=a, min_samples_leaf=c)
        elif(b!=0&c!=0):
            PronosticoAD = DecisionTreeRegressor(min_samples_split=b, min_samples_leaf=c)
        elif(a!=0):
            PronosticoAD = DecisionTreeRegressor(max_depth=a)
        elif(b!=0):
            PronosticoAD = DecisionTreeRegressor(min_samples_split=b)
        elif(c!=0):
            PronosticoAD = DecisionTreeRegressor(min_samples_leaf=c)
        else:
            PronosticoAD = DecisionTreeRegressor()
        PronosticoAD.fit(X_train, Y_train)
        #Pronostico
        Y_Pronostico = PronosticoAD.predict(X_test)
        print(pd.DataFrame(Y_Pronostico))
        Valores = pd.DataFrame(Y_test, Y_Pronostico)
        #print(Valores)
        plt.figure(figsize=(20, 5))
        plt.plot(Y_test, color='green', marker='o', label='Y_test')
        plt.plot(Y_Pronostico, color='red', marker='o', label='Y_Pronostico')
        plt.title('Comparación del modelo con datos reales')
        plt.grid(True)
        plt.legend()
        plt.show()
        ##
        #print('Criterio: \n', PronosticoAD.criterion) 
        #print('Importancia variables: \n', PronosticoAD.feature_importances_)
        #print("MAE: %.4f" % mean_absolute_error(Y_test, Y_Pronostico))
        #print("MSE: %.4f" % mean_squared_error(Y_test, Y_Pronostico))
        #print("RMSE: %.4f" % mean_squared_error(Y_test, Y_Pronostico, squared=False))   #True devuelve MSE, False devuelve RMSE
        #print('Score: %.4f' % r2_score(Y_test, Y_Pronostico))
        ##
        showText.clear()
        showText.append("Criterio: "+str(PronosticoAD.criterion))
        showText.append('Importancia variables: \n'+str(PronosticoAD.feature_importances_))
        showText.append("MAE: "+str(round (mean_absolute_error(Y_test, Y_Pronostico),4)))
        showText.append("MSE: "+str(round(mean_squared_error(Y_test, Y_Pronostico),4)))
        showText.append("RMSE: "+str(round(mean_squared_error(Y_test, Y_Pronostico, squared=False),4)))
        showText.append("Score: "+str(round(r2_score(Y_test, Y_Pronostico),4)))
        ##Niveles del arbol
        plt.figure(figsize=(9,7))  
        plot_tree(PronosticoAD, feature_names = listVar)
        plt.show()
        #
        Reporte = export_text(PronosticoAD, feature_names = listVar)
        #print(Reporte)
        showText2.clear()
        showText2.append(str(Reporte))

    def algoritmoN(self,var,listVar,v1,v2,v3,v4,v5,v6,AreaPronostico):
        #V predictoras
        X=np.array(self.DatosTransacciones[listVar])
        x=pd.DataFrame(X)
        print(x)
        #V a pronosticar
        Y=np.array(self.DatosTransacciones[var])
        y=pd.DataFrame(Y)
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y,test_size=0.2, random_state=1234, shuffle=True)
        print(pd.DataFrame(X_train))
        print(pd.DataFrame(Y_train))
        #Arbol
        PronosticoAD = DecisionTreeRegressor(max_depth=8, min_samples_split=2, min_samples_leaf=8)
        PronosticoAD.fit(X_train, Y_train)
        #Pronostico
        Y_Pronostico = PronosticoAD.predict(X_test)
        print(pd.DataFrame(Y_Pronostico))
        Valores = pd.DataFrame(Y_test, Y_Pronostico)
        print(Valores)
        ##
        print('Criterio: \n', PronosticoAD.criterion) 
        print('Importancia variables: \n', PronosticoAD.feature_importances_)
        print("MAE: %.4f" % mean_absolute_error(Y_test, Y_Pronostico))
        print("MSE: %.4f" % mean_squared_error(Y_test, Y_Pronostico))
        print("RMSE: %.4f" % mean_squared_error(Y_test, Y_Pronostico, squared=False))   #True devuelve MSE, False devuelve RMSE
        print('Score: %.4f' % r2_score(Y_test, Y_Pronostico))
        AreaTumorID1 = pd.DataFrame({'Texture': [v1],'Perimeter': [v2],'Smoothness': [v3],'Compactness': [v4],'Symmetry': [v5],'FractalDimension': [v6]})
        A=round(PronosticoAD.predict(AreaTumorID1)[0],4)
        print(A)
        AreaPronostico.clear()
        AreaPronostico.setText(str(A))