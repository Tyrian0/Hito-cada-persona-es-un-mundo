class ExperienceException(Exception):
    pass

class ExperienceNoValidException(ExperienceException):
    def __init__(this):
        ExperienceException.__init__(this, "experience debe ser un objeto de la clase Experience.")

class IdNoValidException(ExperienceException):
    def __init__(this):
        ExperienceException.__init__(this, "id debe ser una tupla de enteros.")

class NameNoValidException(ExperienceException):
    def __init__(this):
        NameException.__init__(this, "name debe ser un objeto de la clase Experience.")

class TypeNoValidException(ExperienceException):
    def __init__(this):
        ExperienceException.__init__(this, "type debe ser un str.")

class Experience:
    #Constructor
        #id: opcional, si no se incluye no se crea atributo
    def __init__ (this, name, type, id = None):
        if id != None:
            this.setId(id)
        this.__setName(name)
        this.__setType(type)

    #Seter de Id
        #Si id no es un int se lanza una excepción
    def setId(this, id):
        if id == None or type (id) != int:
            raise IdNoValidException()
        this.__id = id
    def getId(this):
        return this.__id

    #Seter de name
        #Si name no es un str lanza una excepción
    def __setName(this, name):
        if name == None or type (name) != str:
            raise NameNoValidException()
        this.__name = name
    def getName(this):
        return this.__name

    #Seter de type
        #Si type no es un str lanza una excepción
        #Es necesario definirlo como _type para poder utilizar la función type
        #type.__class__ = type(type), pero sin problemas de sobreescritura de nombres
    def __setType(this, type):
        if type == None or type.__class__ != str:
            raise TypeNoValidException()
        this.__type = type
    def getType(this):
        return this.__type

    def toJSON (this):
        return {"name": this.getName(),\
                "type": this.getType(),\
                "id": this.getId()}

    def __eq__(self, other): 
        if not isinstance(other, Experience):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.getId() == other.getId()