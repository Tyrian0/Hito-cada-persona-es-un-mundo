import sys
sys.path.append('../')

import mysql.connector
import pandas as pd

from logica.User import *
from logica.MachineLearning import *
from db.AdminUser import *

class AdminMachineLearning:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def getMachineLearning(self):
		query = "SELECT e1.id_exp, e2.id_exp, c.value "  \
				"from correlation_experiences c " \
				"JOIN experiences e1 ON e1.id_exp = c.id_exp1 " \
				"JOIN experiences e2 ON e2.id_exp = c.id_exp2 "
		query = "SELECT * FROM correlation_experiences"
		self.__cursor.execute(query)
		machineLearning_db = self.__cursor.fetchall()
		machineLearning = pd.DataFrame(machineLearning_db, columns=["id_exp1", "id_exp2", "value"])
		print(machineLearning)
		machineLearning1 = machineLearning.pivot(index=['id_exp1'],columns=['id_exp2'],values='value').corr(method='pearson', min_periods=1)
		return machineLearning1

	def calculateCorrelations(self):
		#query = "DELETE FROM correlation_experiences"
		#self.__cursor.execute(query)
		#self.__cnx.commit()
		adminUser = AdminUser()
		#users = adminUser.getAll()
		correlations = self.getMachineLearning()
		machineLearning = MachineLearning(correlations)
		#machineLearning.train(users)
		correlations = machineLearning.getCorrelations()
		table = correlations.melt()
		print(table)
		# for row in correlations.index:
		# 	print(row)
			# id_exp1 = row[0]
			# id_exp2 = row[1]
			# value = row[2]
			# query = "INSERT INTO correlation_experiences(id_exp1, id_exp2, value) " \
			# 		"VALUES (%i, %i, %f)" %(row[0], row[1], row[2])
			# self.__cursor.execute(query)
			# self.__cnx.commit()

	def closeConnection(self):
		self.__cursor.close()
		self.__cnx.close()