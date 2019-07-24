import sys
sys.path.append('../')

import mysql.connector
import pandas as pd
import numpy as np

from logica.User import *
from logica.MachineLearning import *
from db.AdminUser import *

class AdminMachineLearning:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		
	def __getCursor(self):
		return self.__cnx.cursor()		

	def getMachineLearning(self):
		cursor = self.__getCursor()
		query = "SELECT * FROM correlation_experiences"
		cursor.execute(query)
		machineLearning_db = cursor.fetchall()
		corrMatrix = pd.DataFrame(machineLearning_db, columns=["id_exp1", "id_exp2", "value"])
		corrMatrix = corrMatrix.pivot_table(index=['id_exp1'],columns=['id_exp2'],values='value')
		cursor.close()
		return MachineLearning(corrMatrix)

	def calculateCorrelations(self):
		self.deleteCorrelations()
		adminUser = AdminUser()
		users = adminUser.getAll()
		machineLearning = MachineLearning()
		machineLearning.train(users)		
		correlations = machineLearning.getCorrelations()
		for id_exp1, row in correlations.items():
			for id_exp2, value in row.items():
				cursor = self.__getCursor()				
				if id_exp1 == id_exp2:	#Forzamos que la autocorrelación sea 1.
					value = 1.0 		#Esto evita la ideteminación de 0/0 si todas las valoraciones son iguales
				if not np.isnan(value):
					query = "INSERT INTO correlation_experiences(id_exp1, id_exp2, value) " \
								"VALUES (%i, %i, %f)" %(id_exp1, id_exp2, value)
					cursor.execute(query)
					self.__cnx.commit()
					cursor.close()
				

		# for row in correlations.iterrows():
		# 	print (row.shape)
		# 	id_exp1 = row[0]
		# 	n_col = 0
		# 	while n_col < len(row[1]):
		# 		id_exp2 = row[1].keys()[n_col]
		# 		value = row[1].values[n_col]
		# 		if np.isnan(value) == False:
		# 			cursor = self.__getCursor()
		# 			query = "INSERT INTO correlation_experiences(id_exp1, id_exp2, value) " \
		# 					"VALUES (%i, %i, %f)" %(id_exp1, id_exp2, value)
		# 			cursor.execute(query)
		# 			self.__cnx.commit()
		# 			cursor.close()
		# 		n_col += 1

	def deleteCorrelations(self):
		cursor = self.__getCursor()
		query = "DELETE FROM correlation_experiences"
		cursor.execute(query)
		self.__cnx.commit()
		cursor.close()

	def closeConnection(self):
		self.__cnx.close()

