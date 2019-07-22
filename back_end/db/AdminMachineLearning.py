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
		self.__cursor = self.__cnx.cursor()

	def getMachineLearning(self):
		query = "SELECT * FROM correlation_experiences"
		self.__cursor.execute(query)
		machineLearning_db = self.__cursor.fetchall()
		machineLearning = pd.DataFrame(machineLearning_db, columns=["id_exp1", "id_exp2", "value"])
		machineLearning = machineLearning.pivot_table(index=['id_exp1'],columns=['id_exp2'],values='value')
		return machineLearning

	def calculateCorrelations(self):
		self.deleteCorrelations()
		adminUser = AdminUser()
		users = adminUser.getAll()
		print('Num of users: ', len(users))
		machineLearning = MachineLearning()
		machineLearning.train(users)
		correlations = machineLearning.getCorrelations()
		for row in correlations.iterrows():
			id_exp1 = row[0]
			n_col = 0
			print(len(row[1]))
			while n_col < len(row[1]):
				id_exp2 = row[1].keys()[n_col]
				value = row[1].values[n_col]
				if np.isnan(value) == False:
					query = "INSERT INTO correlation_experiences(id_exp1, id_exp2, value) " \
							"VALUES (%i, %i, %f)" %(id_exp1, id_exp2, value)
					print(query)
					self.__cursor.execute(query)
					self.__cnx.commit()
				n_col += 1

	def deleteCorrelations(self):
		query = "DELETE FROM correlation_experiences"
		self.__cursor.execute(query)
		self.__cnx.commit()