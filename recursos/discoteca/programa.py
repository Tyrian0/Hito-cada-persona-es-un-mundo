from clases.genero import Genero
from db.AdminGenero import AdminGenero
from clases.discografica import Discografica
from db.AdminDiscografica import AdminDiscografica
from clases.cd import Cd
from db.AdminCd import AdminCd

#Funcion comprobar fecha
def isFecha(fecha):
  diasMes = (31,29,31,30,31,30,31,31,30,31,30,31)
  anyoActual = 2019
  return type(fecha) is str and len(fecha)==10 and fecha[4]  == "/" and fecha[7]  == "/"\
   and fecha[0:4].isdigit() and fecha[5:7].isdigit() and fecha[8:10].isdigit() \
   and int (fecha[0:4]) > 0 and int (fecha[0:4]) <= anyoActual \
   and int(fecha[5:7]) > 0 and int(fecha[5:7]) < 13 and int(fecha[8:10]) <= diasMes[int(fecha[5:7])-1]
    
MENU_PRINCIPAL = """1. Administrar Genero
2. Administrar Discograficas
3. Administrar CD
0. Salir
"""
MENU_GENERO = """1. Insertar
2. Actualizar
3. Listar
4. Borrar
0. Salir
"""
MENU_DISCOGRAFICA = """1. Insertar
2. Actualizar
3. Listar
4. Borrar
0. Salir
"""
MENU_CD = """1. Insertar
2. Actualizar
3. Listar
4. Borrar
0. Salir
"""
MENU_CD_ACTUALIZAR = """1. Nombre
2. Fecha
3. Discografica
4. Añadir generos
5. Eliminar generos
0. Guardar cambios
"""

#logica de generos
def gestionarGeneros():
  adminGenero = AdminGenero()
  opcionGenero = ""
  while not opcionGenero == "0":
    opcionGenero = input (MENU_GENERO)
    if opcionGenero == "1":
      insertarGenero(adminGenero)
    elif opcionGenero == "2":
      actualizarGenero(adminGenero)
    elif opcionGenero == "3":
      listarGenero(adminGenero)
    elif opcionGenero == "4":
      borrarGenero(adminGenero)
    elif opcionGenero == "0":
      print ("Volviendo al menu principal...")
    else:
      print ("Opcion no válida.")
  adminGenero.cerrarCnx()

def insertarGenero(adminGenero):
  genero = input ("Introduce el nuevo genero: ")
  adminGenero.crear(Genero(genero))

def actualizarGenero(adminGenero):
  generos = adminGenero.getAll()
  printGeneros(generos)
  generoAntiguo = input ("Introduce el genero que deseas modificar: ")
  for genero in generos:
    if generoAntiguo==genero.getNombre():
      genero.setNombre(input ("Introduce el nuevo genero: "))
      adminGenero.actualizar(genero)
      break
  else:
    print("No existe ese genero!")
def printGeneros(generos):
  #print ("ID\tGenero")
  print ("Genero")
  for genero in generos:
    print (genero)
  
def listarGenero(adminGenero):
  printGeneros(adminGenero.getAll())
    
def borrarGenero(adminGenero):
  generos = adminGenero.getAll()
  printGeneros(generos)
  generoAntiguo = input ("Introduce el genero que deseas borrar: ")
  for genero in generos:
    if generoAntiguo==genero.getNombre():
      adminGenero.borrar(genero)
      break
  else:
    print("No existe ese genero!")

#Logica de discografica
def gestionarDiscograficas():
  adminDiscografica = AdminDiscografica()
  opcionDiscografica = ""
  while not opcionDiscografica == "0":
    opcionDiscografica = input (MENU_DISCOGRAFICA)
    if opcionDiscografica == "1":
      insertarDiscografica(adminDiscografica)
    elif opcionDiscografica == "2":
      actualizarDiscografica(adminDiscografica)
    elif opcionDiscografica == "3":
      listarDiscografica(adminDiscografica)
    elif opcionDiscografica == "4":
      borrarDiscografica(adminDiscografica)
    elif opcionDiscografica == "0":
      print ("Volviendo al menu principal...")
    else:
      print ("Opcion no válida.")
  adminDiscografica.cerrarCnx()

def insertarDiscografica(adminDiscografica):
  discografica = input ("Introduce el nuevo discografica: ")
  adminDiscografica.crear(Discografica(discografica))

def actualizarDiscografica(adminDiscografica):
  discograficas = adminDiscografica.getAll()
  printDiscograficas(discograficas)
  discograficaAntiguo = input ("Introduce el discografica que deseas modificar: ")
  for discografica in discograficas:
    if discograficaAntiguo==discografica.getNombre():
      discografica.setNombre(input ("Introduce el nuevo discografica: "))
      adminDiscografica.actualizar(discografica)
      break
  else:
    print("No existe ese discografica!")
def printDiscograficas(discograficas):
  #print ("ID\tDiscografica")
  print ("Discografica")
  for discografica in discograficas:
    print (discografica)
  
def listarDiscografica(adminDiscografica):
  printDiscograficas(adminDiscografica.getAll())
    
def borrarDiscografica(adminDiscografica):
  discograficas = adminDiscografica.getAll()
  printDiscograficas(discograficas)
  discograficaAntiguo = input ("Introduce el discografica que deseas borrar: ")
  for discografica in discograficas:
    if discograficaAntiguo==discografica.getNombre():
      adminDiscografica.borrar(discografica)
      break
  else:
    print("No existe ese discografica!")

#logica de cd
def gestionarCds():
  adminCd = AdminCd()
  adminDiscografica = AdminDiscografica()
  adminGenero = AdminGenero()
  opcionCd = ""
  while not opcionCd == "0":
    opcionCd = input (MENU_CD)
    if opcionCd == "1":
      insertarCd(adminCd, adminDiscografica, adminGenero)
    elif opcionCd == "2":
      actualizarCd(adminCd, adminDiscografica, adminGenero)
    elif opcionCd == "3":
      listarCd(adminCd)
    elif opcionCd == "4":
      borrarCd(adminCd)
    elif opcionCd == "0":
      print ("Volviendo al menu principal...")
    else:
      print ("Opcion no válida.")
  adminCd.cerrarCnx()
  adminDiscografica.cerrarCnx()
  adminGenero.cerrarCnx()

def insertarCd(adminCd,adminDiscografica, adminGenero):
  nombre = input ("Introduce el nuevo nombre: ")
  
  fecha = input ("Introduce la fecha (yyyy/mm/dd): ")
  while not isFecha(fecha):
    print("Fecha invalida.")
    fecha = input ("Introduce la fecha (yyyy/mm/dd): ")
    
  generosTodos = adminGenero.getAll()
  generos = []
  continuar = "S"
  while continuar == "S":
    printGeneros(generosTodos)
    generoNombre = input ("Introduce el genero que deseas añadir: ")
    for genero in generosTodos:
      if generoNombre==genero.getNombre():
        generos.append(genero)
        continuar = input ("Desea añadir más generos (S/N): ") #Cualquier cosa que no sea "S" es interpretado como "N"
        break
      else:
        print("No existe ese genero!")
        
  discograficas = adminDiscografica.getAll()
  discograficaValida = False
  while not discograficaValida:
    printDiscograficas(discograficas)
    discograficaNombre = input("Introduce el nombre de la discografica: ")
    for discografica in discograficas:
      if discograficaNombre==discografica.getNombre():      
        print(Cd(nombre, fecha, discografica, generos = generos))
        adminCd.crear(Cd(nombre, fecha, discografica, generos = generos))
        discograficaValida = True
        break
    else:
      print("No existe esa discografica!")


def actualizarCd(adminCd, adminDiscografica, adminGenero):
  cds = adminCd.getAll()
  printCds(cds)
  cdAntiguo = input ("Introduce el cd que deseas modificar: ")
  for cd in cds:
    if cdAntiguo==cd.getNombre():
      discografica = cd.getDiscografica
      opcionActualizarCD = ""
      while opcionActualizarCD != "0":
        opcionActualizarCD =input(MENU_CD_ACTUALIZAR)
        if opcionActualizarCD == "1":
          nombre = input ("Introduce el nuevo nombre: ")
          cd.setNombre(nombre)
        elif opcionActualizarCD == "2":
          fecha = input ("Introduce la nueva fecha (yyyy/mm/dd): ")
          while not isFecha(fecha):
            print ("Fecha no válida")
            fecha = input ("Introduce la nueva fecha (yyyy/mm/dd): ")
          cd.setAnyo(fecha)
        elif opcionActualizarCD == "3":
          discograficas = adminDiscografica.getAll()
          printDiscograficas(discograficas)
          nuevaDiscografica = input("Introduce el nombre de la discografica: ")
          for discografica in discograficas:
           if nuevaDiscografica == discografica.getNombre():
              cd.setDiscografica(discografica)
              break
          else:
            print("No existe esa discografica!")
        elif opcionActualizarCD == "4":
          generosTodos = adminGenero.getAll()
          continuar = "S"
          while continuar == "S":
            printGeneros(generosTodos)
            generoNombre = input ("Introduce el genero que deseas añadir: ")
            for genero in generosTodos:
          	  if generoNombre==genero.getNombre():
          	  	cd.addGenero(genero)
          	  	break
            else:
          	  print("No existe ese genero!")
            continuar = input ("Desea añadir más generos (S/N): ") #Cualquier cosa que no sea "S" es interpretado como "N"
        elif opcionActualizarCD == "5":
          continuar = "S"
          while continuar == "S":
            printGeneros(cd.getGeneros())
            generoNombre = input ("Introduce el genero que deseas eliminar: ")
            for genero in cd.getGeneros():
          	  if generoNombre==genero.getNombre():
          	  	cd.removeGenero(genero)
          	  	break
            else:
          	  print("No existe ese genero!")
            continuar = input ("Desea borrar más géneros (S/N): ") #Cualquier cosa que no sea "S" es interpretado como "N"
        elif opcionActualizarCD == "0":
        	print ("Salvando...")
        else:
          print ("Opcion no válida.")
      adminCd.actualizar(cd)
      break
  else:
    print("No existe ese cd!")

def printCds(cds):
  print ("%-45s\t%-10s\t%-20s\tGeneros" %("CD", "Año","Discografica"))
  print ("-"*100)
  for cd in cds:
    print (cd)
  
def listarCd(adminCd):
  printCds(adminCd.getAll())
    
def borrarCd(adminCd):
  cds = adminCd.getAll()
  printCds(cds)
  cdAntiguo = input ("Introduce el cd que deseas borrar: ")
  for cd in cds:
    if cdAntiguo==cd.getNombre():
      adminCd.borrar(cd)
      break
  else:
    print("No existe ese cd!")

#main 
opcionPrincipal = ""
while not opcionPrincipal == "0":
  opcionPrincipal = input (MENU_PRINCIPAL)
  if opcionPrincipal == "1":
    gestionarGeneros()
  if opcionPrincipal == "2":
    gestionarDiscograficas()
  if opcionPrincipal == "3":
    gestionarCds()
  elif opcionPrincipal == "0":
    print ("Saliendo...")
  else:
    print ("Opcion no válida.")
