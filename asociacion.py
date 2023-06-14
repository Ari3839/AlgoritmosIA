import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from apyori import apriori

class AlgoritApriori:
    def __init__(self,name):
        self.name = name
        self.DatosTransacciones = pd.read_csv(self.name, header=None)
    
    def graficaFrecuencia(self):        
        Transacciones=self.DatosTransacciones.values.reshape(-1).tolist()
        Lista=pd.DataFrame(Transacciones)
        Lista['Frecuencia']=1
        Lista=Lista.groupby(by=[0],as_index=False).count().sort_values(by=['Frecuencia'],ascending=True)
        Lista['Porcentaje']=(Lista['Frecuencia']/Lista['Frecuencia'].sum())
        Lista=Lista.rename(columns={0:'Item'})
        #print(Lista)
        plt.figure(figsize=(10,18))
        plt.ylabel('Item')
        plt.xlabel('Frecuencia')
        plt.barh(Lista['Item'],width=Lista['Frecuencia'],color='purple')
        plt.show()

    def algoritmo(self, soporte, confianza, elevacion, Resultados):
        MoviesLista = self.DatosTransacciones.stack().groupby(level=0).apply(list).tolist()
        #print(MoviesLista)
        ReglasC1 = apriori(MoviesLista,min_support=soporte,min_confidence=confianza,min_lift=elevacion)
        ResultadosC1 = list(ReglasC1)
        #print(ResultadosC1)
        #return ResultadosC1
        for item in ResultadosC1:
            Emparejar = item[0]
            items = [x for x in Emparejar]
            Resultados.append("Regla: " + str(item[0]))
            #print("Regla: " + str(item[0]))
            Resultados.append("Soporte: " + str(item[1]))
            #print("Soporte: " + str(item[1]))
            Resultados.append("Confianza: " + str(item[2][0][2]))
            #print("Confianza: " + str(item[2][0][2]))
            Resultados.append("Lift: " + str(item[2][0][3])) 
            #print("Lift: " + str(item[2][0][3])) 
            Resultados.append("=====================================")
            #print("=====================================") 