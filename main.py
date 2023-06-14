import sys
import pandas as pd
from scipy.cluster.hierarchy import centroid
from GUI_ui import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from Custom_Widgets.Widgets import *
from asociacion import AlgoritApriori
from cluster_part import ClusterPart
from distancias import Distances
from cluster_jer import ClusterJer
from cluster_part import ClusterPart
from RegresionLog import RLogistica
from RegresionLogN import RLogisticaN
from arbolP import ArbolP
from arbolC import ArbolC

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()
		########################################################################
		# APPLY JSON STYLESHEET
		########################################################################
		# self = QMainWindow class
		# self.ui = Ui_MainWindow / user interface class
		loadJsonStyle(self, self.ui)
		########################################################################
		self.ui.browse.clicked.connect(self.browsefiles)
		self.ui.limpiar.clicked.connect(self.cleaner)
		self.ui.limpiar_2.clicked.connect(self.cleanerApriori)
		self.ui.Button_2.clicked.connect(self.graficaFrec)
		self.ui.calcular.clicked.connect(self.results)
		self.ui.guardar.clicked.connect(self.guardarDatos)
		self.ui.Euclideana.clicked.connect(self.metricDist1)
		self.ui.Chebyshev.clicked.connect(self.metricDist2)
		self.ui.Manhattan.clicked.connect(self.metricDist3)
		self.ui.Minkowski.clicked.connect(self.metricDist4)
		self.ui.Button_3.clicked.connect(self.infoData)
		self.ui.EvalVis_Button.clicked.connect(self.GrafEvalVisual)
		self.ui.MCorr_Button.clicked.connect(self.Correlacion)
		self.ui.Tree_Button.clicked.connect(self.tree)
		self.ui.Centro_Button.clicked.connect(self.centroide)
		self.ui.Button_4.clicked.connect(self.infoData2)
		self.ui.EvalVis_Button_2.clicked.connect(self.GrafEvalVisual2)
		self.ui.MCorr_Button_2.clicked.connect(self.Correlacion2)
		self.ui.Elbow_Button_2.clicked.connect(self.elbowM)
		self.ui.Centro_Button_2.clicked.connect(self.centroide2)
		self.ui.Button_6.clicked.connect(self.infoData3)
		self.ui.EvalVis_Button_3.clicked.connect(self.GrafEvalVisual3)
		self.ui.MCorr_Button_3.clicked.connect(self.Correlacion3)
		self.ui.RL_Button.clicked.connect(self.RegLog)
		self.ui.Diagnosis_button.clicked.connect(self.RegLogN)
		self.ui.Button_8.clicked.connect(self.GTemp)
		self.ui.TreeB.clicked.connect(self.arbolPronos)
		self.ui.AreaButton_2.clicked.connect(self.ArbolPN)
		self.ui.Button_10.clicked.connect(self.GTemp2)
		self.ui.TreeB_2.clicked.connect(self.arbolClas)
		self.ui.Diagnosis_button_2.clicked.connect(self.ArbolCN)

	def browsefiles(self):
		fname, _=QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*.csv')
		self.ui.filename.setText(fname)
		if(os.path.exists(self.ui.filename.text())):
			with open(fname,'r') as file:
				df=pd.read_csv(fname,header=None)
				#print(df)
				self.ui.tableWidget.setColumnCount(len(df.columns))
				self.ui.tableWidget.setRowCount(len(df.index))
				for i in range(len(df.index)):
					for j in range(len(df.columns)):
						self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))

	def graficaFrec(self):
		if(len(self.ui.filename.text())!=0):
			AlgoritApriori(self.ui.filename.text()).graficaFrecuencia()
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def cleaner(self):
		self.ui.tableWidget.clear()
		self.ui.tableWidget_2.clear()
		self.ui.tableWidget_3.clear()
		self.ui.tableWidget_4.clear()
		self.ui.tableWidget_5.clear()
		self.ui.filename.setText('')
		self.ui.ShowText.clear()
		self.ui.ShowText_2.clear()
		self.ui.ShowText_3.clear()
		self.ui.textura_line.setText('')
		self.ui.area_line.setText('')
		self.ui.Smoothness_line.setText('')
		self.ui.Comp_line.setText('')
		self.ui.sym_line.setText('')
		self.ui.fractal_line.setText('')
		self.ui.DiagnosisLineEdit.setText('')
		self.ui.ID_line.setText('')
		self.ui.ShowText_5.clear()
		self.ui.ShowText_6.clear()
		self.ui.predictora.setText('')
		self.ui.depth.setText('')
		self.ui.minleaf.setText('')
		self.ui.minSplit.setText('')
		self.ui.textura_line_2.setText('')
		self.ui.Perimeter_line_2.setText('')
		self.ui.Smoothness_line_2.setText('')
		self.ui.Comp_line_2.setText('')
		self.ui.sym_line_2.setText('')
		self.ui.fractal_line_2.setText('')
		self.ui.AreaC.setText('')
		self.ui.ID_line_2.setText('')
		self.ui.ShowText_7.clear()
		self.ui.ShowText_8.clear()
		self.ui.predictora_2.setText('')
		self.ui.depth_2.setText('')
		self.ui.minleaf_2.setText('')
		self.ui.minSplit_2.setText('')
		self.ui.textura_line_4.setText('')
		self.ui.area_line_2.setText('')
		self.ui.Smoothness_line_4.setText('')
		self.ui.Comp_line_4.setText('')
		self.ui.sym_line_4.setText('')
		self.ui.fractal_line_4.setText('')
		self.ui.DiagnosisLineEdit_2.setText('')
		self.ui.ID_line_4.setText('')

	def cleanerApriori(self):
		self.ui.Resultados.clear()
		self.ui.Soporte.setText('')
		self.ui.Confianza.setText('')
		self.ui.Elevacion.setText('')

	def results(self):
		if((len(self.ui.Soporte.text())!=0)&(len(self.ui.Confianza.text()))!=0&(len(self.ui.Elevacion.text())!=0)):
			sop=float(self.ui.Soporte.text())
			conf=float(self.ui.Confianza.text())
			elev=float(self.ui.Elevacion.text())
			if((isinstance(sop, float))&(isinstance(sop, float))&(isinstance(elev, float))):
				AlgoritApriori(self.ui.filename.text()).algoritmo(sop,conf,elev,self.ui.Resultados)
			else:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Warning)
				msg.setText("Wait")
				msg.setInformativeText('Los datos deben ser valores numericos')
				msg.setWindowTitle("Upps")
				msg.exec_()
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Necesitas ingresar datos para soporte, confianza y elevación')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def guardarDatos(self):
		f=open("ReglasAsociacion.txt","w")
		f.write(self.ui.Resultados.toPlainText())
		f.close()

	def metricDist1(self):
		if(len(self.ui.filename.text())!=0):
			self.ui.tableWidget_2.clear()
			MEuclidiana=Distances(self.ui.filename.text()).MatrizEclideana()
			self.ui.tableWidget_2.setColumnCount(len(MEuclidiana.columns))
			self.ui.tableWidget_2.setRowCount(len(MEuclidiana.index))
			for i in range(len(MEuclidiana.index)):
				for j in range(len(MEuclidiana.columns)):
					self.ui.tableWidget_2.setItem(i,j,QTableWidgetItem(str(MEuclidiana.iloc[i, j])))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def metricDist2(self):
		if(len(self.ui.filename.text())!=0):
			self.ui.tableWidget_2.clear()
			MCheb=Distances(self.ui.filename.text()).MatrizChebyshev()
			self.ui.tableWidget_2.setColumnCount(len(MCheb.columns))
			self.ui.tableWidget_2.setRowCount(len(MCheb.index))
			for i in range(len(MCheb.index)):
				for j in range(len(MCheb.columns)):
					self.ui.tableWidget_2.setItem(i,j,QTableWidgetItem(str(MCheb.iloc[i, j])))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()
		

	def metricDist3(self):
		if(len(self.ui.filename.text())!=0):
			self.ui.tableWidget_2.clear()
			MManhattan=Distances(self.ui.filename.text()).MatrizManhattan()
			self.ui.tableWidget_2.setColumnCount(len(MManhattan.columns))
			self.ui.tableWidget_2.setRowCount(len(MManhattan.index))
			for i in range(len(MManhattan.index)):
				for j in range(len(MManhattan.columns)):
					self.ui.tableWidget_2.setItem(i,j,QTableWidgetItem(str(MManhattan.iloc[i, j])))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def metricDist4(self):
		if(len(self.ui.filename.text())!=0):
			self.ui.tableWidget_2.clear()
			MMin=Distances(self.ui.filename.text()).MatrizMinkowski()
			self.ui.tableWidget_2.setColumnCount(len(MMin.columns))
			self.ui.tableWidget_2.setRowCount(len(MMin.index))
			for i in range(len(MMin.index)):
				for j in range(len(MMin.columns)):
					self.ui.tableWidget_2.setItem(i,j,QTableWidgetItem(str(MMin.iloc[i, j])))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def infoData(self):
		if(len(self.ui.filename.text())!=0):
			ClusterJer(self.ui.filename.text()).infoD(self.ui.ShowText)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def GrafEvalVisual(self):
		if(len(self.ui.filename.text())!=0):
			ClusterJer(self.ui.filename.text()).evalVisual(self.ui.varLine.text())
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def Correlacion(self):
		if(len(self.ui.filename.text())!=0):
			pdM=ClusterJer(self.ui.filename.text()).MCorrelaciones()
			#print(pdM)
			self.ui.tableWidget_3.setColumnCount(len(pdM.columns))
			self.ui.tableWidget_3.setRowCount(len(pdM.index))
			for i in range(len(pdM.index)):
				for j in range(len(pdM.columns)):
					self.ui.tableWidget_3.setItem(i,j,QTableWidgetItem(str(pdM.iloc[i, j])))
			with open(self.ui.filename.text(),'r') as file:
				df=list(pd.read_csv(self.ui.filename.text(),nrows=1,header=0))
				print(df)
			self.ui.ShowText.clear()
			for line in df:
				self.ui.ShowText.append(line)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def tree(self):
		if(len(self.ui.ShowText.toPlainText())!=0):
			labelX="Eje X"
			labelY="Eje Y"
			NumClust=0
			var=self.ui.ShowText.toPlainText().replace('\n',',')
			listVar=var.split(',')
			#print(listVar)
			if(len(self.ui.xLabel.text())!=0):
				labelX=self.ui.xLabel.text()
			if(len(self.ui.YLabel.text())!=0):
				labelY=self.ui.YLabel.text()
			if(len(self.ui.NoClusters.text())!=0):
				NumClust=int(self.ui.NoClusters.text())
			ClusterJer(self.ui.filename.text()).arbol(listVar,labelX,labelY,NumClust)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def centroide(self):
		if(len(self.ui.ShowText.toPlainText())!=0):
			NumClust=2
			Variable=""
			var=self.ui.ShowText.toPlainText().replace('\n',',')
			listVar=var.split(',')
			if(len(self.ui.NoClusters.text())!=0):
				NumClust=int(self.ui.NoClusters.text())
			if(len(self.ui.varLine.text())!=0):
				Variable=self.ui.varLine.text()
			Centroides=ClusterJer(self.ui.filename.text()).Cent(NumClust,Variable,self.ui.ShowText,listVar)
			self.ui.tableWidget_3.setColumnCount(len(Centroides.columns))
			self.ui.tableWidget_3.setRowCount(len(Centroides.index))
			for i in range(len(Centroides.index)):
				for j in range(len(Centroides.columns)):
					self.ui.tableWidget_3.setItem(i,j,QTableWidgetItem(str(Centroides.iloc[i, j])))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()
	
	def infoData2(self):
		if(len(self.ui.filename.text())!=0):
			ClusterPart(self.ui.filename.text()).infoD(self.ui.ShowText_2)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def GrafEvalVisual2(self):
		if(len(self.ui.filename.text())!=0):
			ClusterPart(self.ui.filename.text()).evalVisual(self.ui.varLine_2.text())
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def Correlacion2(self):
		if(len(self.ui.filename.text())!=0):
			pdM=ClusterPart(self.ui.filename.text()).MCorrelaciones()
			#print(pdM)
			self.ui.tableWidget_4.setColumnCount(len(pdM.columns))
			self.ui.tableWidget_4.setRowCount(len(pdM.index))
			for i in range(len(pdM.index)):
				for j in range(len(pdM.columns)):
					self.ui.tableWidget_4.setItem(i,j,QTableWidgetItem(str(pdM.iloc[i, j])))
			with open(self.ui.filename.text(),'r') as file:
				df=list(pd.read_csv(self.ui.filename.text(),nrows=1,header=0))
				print(df)
			self.ui.ShowText_2.clear()
			for line in df:
				self.ui.ShowText_2.append(line)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def elbowM(self):
		if(len(self.ui.ShowText_2.toPlainText())!=0):
			var=self.ui.ShowText_2.toPlainText().replace('\n',',')
			listVar=var.split(',')
			#print(listVar)
			ClusterPart(self.ui.filename.text()).elbow(listVar)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def centroide2(self):
		if(len(self.ui.ShowText_2.toPlainText())!=0):
			Variable=""
			var=self.ui.ShowText_2.toPlainText().replace('\n',',')
			listVar=var.split(',')
			if(len(self.ui.varLine_2.text())!=0):
				Variable=self.ui.varLine_2.text()
			Centroides=ClusterPart(self.ui.filename.text()).Cent(Variable,self.ui.ShowText_2,listVar)
			self.ui.tableWidget_4.setColumnCount(len(Centroides.columns))
			self.ui.tableWidget_4.setRowCount(len(Centroides.index))
			for i in range(len(Centroides.index)):
				for j in range(len(Centroides.columns)):
					self.ui.tableWidget_4.setItem(i,j,QTableWidgetItem(str(Centroides.iloc[i, j])))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()
	
	def infoData3(self):
		if(len(self.ui.filename.text())!=0):
			RLogistica(self.ui.filename.text()).infoD(self.ui.ShowText_3)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def GrafEvalVisual3(self):
		if(len(self.ui.filename.text())!=0):
			RLogistica(self.ui.filename.text()).evalVisual(self.ui.varLine_3.text())
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def Correlacion3(self):
		if(len(self.ui.filename.text())!=0):
			pdM=RLogistica(self.ui.filename.text()).MCorrelaciones()
			#print(pdM)
			self.ui.tableWidget_5.setColumnCount(len(pdM.columns))
			self.ui.tableWidget_5.setRowCount(len(pdM.index))
			for i in range(len(pdM.index)):
				for j in range(len(pdM.columns)):
					self.ui.tableWidget_5.setItem(i,j,QTableWidgetItem(str(pdM.iloc[i, j])))
			with open(self.ui.filename.text(),'r') as file:
				df=list(pd.read_csv(self.ui.filename.text(),nrows=1,header=0))
				print(df)
			self.ui.ShowText_3.clear()
			for line in df:
				self.ui.ShowText_3.append(line)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def RegLog(self):
		Num=0.2
		if(len(self.ui.ShowText_3.toPlainText())!=0):
			if(len(self.ui.varLine_3.text())!=0):
				Variable=self.ui.varLine_3.text()
				var=self.ui.ShowText_3.toPlainText().replace('\n',',')
				listVar=var.split(',')
				if(len(self.ui.NoClusters_2.text())!=0):
					Num=float(self.ui.NoClusters_2.text())
				MC=RLogistica(self.ui.filename.text()).algoritmo(Variable,listVar,Num,self.ui.ShowText_3)
				self.ui.tableWidget_5.setColumnCount(len(MC.columns))
				self.ui.tableWidget_5.setRowCount(len(MC.index))
				for i in range(len(MC.index)):
					for j in range(len(MC.columns)):
						self.ui.tableWidget_5.setItem(i,j,QTableWidgetItem(str(MC.iloc[i, j])))
			else:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Warning)
				msg.setText("Wait")
				msg.setInformativeText('Debes seleccionar una variable de clase')
				msg.setWindowTitle("Upps")
				msg.exec_()
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def RegLogN(self):
		Num=0.2
		valoresList=[]
		if((len(self.ui.ID_line.text())!=0)&(len(self.ui.textura_line.text())!=0)&(len(self.ui.area_line.text())!=0)&(len(self.ui.Smoothness_line.text())!=0)&(len(self.ui.Comp_line.text())!=0)&(len(self.ui.sym_line.text())!=0)&(len(self.ui.fractal_line.text())!=0)):
			variable='Diagnosis'
			listVar=['Texture','Area','Smoothness','Compactness','Symmetry','FractalDimension']
			valoresList.append(float(self.ui.textura_line.text()))
			valoresList.append(float(self.ui.area_line.text()))
			valoresList.append(float(self.ui.Smoothness_line.text()))
			valoresList.append(float(self.ui.Comp_line.text()))
			valoresList.append(float(self.ui.sym_line.text()))
			valoresList.append(float(self.ui.fractal_line.text()))
			RLogisticaN('WDBCOriginal.csv').algoritmoN(variable,listVar,Num,self.ui.DiagnosisLineEdit,valoresList)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Debes ingresar todos los datos')
			msg.setWindowTitle("Upps")
			msg.exec_()
	
	def GTemp(self):
		if(len(self.ui.filename.text())!=0):
			ArbolP(self.ui.filename.text()).MTemp()
			with open(self.ui.filename.text(),'r') as file:
				df=list(pd.read_csv(self.ui.filename.text(),nrows=1,header=0))
				print(df)
			self.ui.ShowText_5.clear()
			for line in df:
				self.ui.ShowText_5.append(line)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def arbolPronos(self):
		a=0
		b=0
		c=0
		Num=0.2
		var=""
		listVar=[]
		if(len(self.ui.ShowText_5.toPlainText())!=0):
			if(len(self.ui.predictora.text())!=0):
				Variable=self.ui.predictora.text()
				var=self.ui.ShowText_5.toPlainText().replace('\n',',')
				listVar=var.split(',')
				if(len(self.ui.depth.text())!=0):
					a=int(self.ui.depth.text())
				if(len(self.ui.minSplit.text())!=0):
					b=int(self.ui.minSplit.text())
				if(len(self.ui.minleaf.text())!=0):
					c=int(self.ui.minleaf.text())
				if(len(self.ui.numL.text())!=0):
					Num=float(self.ui.numL.text())
				ArbolP(self.ui.filename.text()).algoritmo(Variable,listVar,self.ui.ShowText_5,self.ui.ShowText_6,a,b,c,Num)
			else:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Warning)
				msg.setText("Wait")
				msg.setInformativeText('Debes seleccionar una variable predictora')
				msg.setWindowTitle("Upps")
				msg.exec_()
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def ArbolPN(self):
		if((len(self.ui.ID_line_2.text())!=0)&(len(self.ui.textura_line_2.text())!=0)&(len(self.ui.Perimeter_line_2.text())!=0)&(len(self.ui.Smoothness_line_2.text())!=0)&(len(self.ui.Comp_line_2.text())!=0)&(len(self.ui.sym_line_2.text())!=0)&(len(self.ui.fractal_line_2.text())!=0)):
			variable='Area'
			listVar=['Texture','Perimeter','Smoothness','Compactness','Symmetry','FractalDimension']
			v1=float(self.ui.textura_line_2.text())
			v2=float(self.ui.Perimeter_line_2.text())
			v3=float(self.ui.Smoothness_line_2.text())
			v4=float(self.ui.Comp_line_2.text())
			v5=float(self.ui.sym_line_2.text())
			v6=float(self.ui.fractal_line_2.text())
			ArbolP('WDBCOriginal.csv').algoritmoN(variable,listVar,v1,v2,v3,v4,v5,v6,self.ui.AreaC)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Debes ingresar todos los datos')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def GTemp2(self):
		if(len(self.ui.filename.text())!=0):
			ArbolC(self.ui.filename.text()).MTemp()
			with open(self.ui.filename.text(),'r') as file:
				df=list(pd.read_csv(self.ui.filename.text(),nrows=1,header=0))
				print(df)
			self.ui.ShowText_7.clear()
			for line in df:
				self.ui.ShowText_7.append(line)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def arbolClas(self):
		a=0
		b=0
		c=0
		Num=0.2
		var=""
		listVar=[]
		if(len(self.ui.ShowText_7.toPlainText())!=0):
			if(len(self.ui.predictora_2.text())!=0):
				Variable=self.ui.predictora_2.text()
				var=self.ui.ShowText_7.toPlainText().replace('\n',',')
				listVar=var.split(',')
				if(len(self.ui.depth_2.text())!=0):
					a=int(self.ui.depth_2.text())
				if(len(self.ui.minSplit_2.text())!=0):
					b=int(self.ui.minSplit_2.text())
				if(len(self.ui.minleaf_2.text())!=0):
					c=int(self.ui.minleaf_2.text())
				if(len(self.ui.numL_2.text())!=0):
					Num=float(self.ui.numL_2.text())
				MC=ArbolC(self.ui.filename.text()).algoritmo(Variable,listVar,self.ui.ShowText_7,self.ui.ShowText_8,a,b,c,Num)
				self.ui.tableWidget_7.setColumnCount(len(MC.columns))
				self.ui.tableWidget_7.setRowCount(len(MC.index))
				for i in range(len(MC.index)):
					for j in range(len(MC.columns)):
						self.ui.tableWidget_7.setItem(i,j,QTableWidgetItem(str(MC.iloc[i, j])))
			else:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Warning)
				msg.setText("Wait")
				msg.setInformativeText('Debes seleccionar una variable predictora')
				msg.setWindowTitle("Upps")
				msg.exec_()
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Selecciona un archivo primero')
			msg.setWindowTitle("Upps")
			msg.exec_()

	def ArbolCN(self):
		if((len(self.ui.ID_line_4.text())!=0)&(len(self.ui.textura_line_4.text())!=0)&(len(self.ui.area_line_2.text())!=0)&(len(self.ui.Smoothness_line_4.text())!=0)&(len(self.ui.Comp_line_4.text())!=0)&(len(self.ui.sym_line_4.text())!=0)&(len(self.ui.fractal_line_4.text())!=0)):
			variable='Diagnosis'
			listVar=['Texture','Area','Smoothness','Compactness','Symmetry','FractalDimension']
			v1=float(self.ui.textura_line_4.text())
			v2=float(self.ui.area_line_2.text())
			v3=float(self.ui.Smoothness_line_4.text())
			v4=float(self.ui.Comp_line_4.text())
			v5=float(self.ui.sym_line_4.text())
			v6=float(self.ui.fractal_line_4.text())
			ArbolC('WDBCOriginal.csv').algoritmoN(variable,listVar,v1,v2,v3,v4,v5,v6,self.ui.DiagnosisLineEdit_2)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Wait")
			msg.setInformativeText('Debes ingresar todos los datos')
			msg.setWindowTitle("Upps")
			msg.exec_()

if __name__ =="__main__":
	app=QApplication(sys.argv)
	window=MainWindow()
	window.show()
	sys.exit(app.exec_())