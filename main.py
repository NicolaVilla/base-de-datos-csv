import csv
class BaseDeDatos():
    def __init__(self,file_name):
        self.path = "./archivos/" + file_name +".csv"
    #metodo para pedir los datos 
    def ingresar_datos(self):
        datos = []
        with open (self.path,"r") as file:
            reader = list(csv.reader(file, skipinitialspace=True))
            campos = reader[0]
            datos.append(len(reader))
            for i in range(1,len(campos)):
                dato = input("Ingrese el "+campos[i]+" del usuario: ")
                datos.append(dato)
        return datos

    #funcion para agregar un nueva linea a la base de datos, utiliza el metodo ingresar_datos
    def crear_usuario(self):   
        datos = self.ingresar_datos()
        with open(self.path,"a") as file:
            writer = csv.writer(file)
            file.write("\n")
            writer.writerow(datos)
    
    #Metodo que devuelve una lista con todos los datos de la base
    def extraer_datos(self):
        datos = []
        with open(self.path,"r") as file:
            datos = list(csv.reader(file, skipinitialspace=True))
        return datos
    
    #metodo que permite actualizar la base de datos
    def actualizar_usuario(self):
        id = int(input("Ingrese la id del usuario que desea actualizar: "))
        datos = self.extraer_datos()
        for i in range(1,len(datos)):
            if(int(datos[i][0]) == id):
                datos[i] = self.ingresar_datos()
                datos[i][0] = id
        self.cargar_datos(datos)

    #def borrar_usuario(self):
        
    #def borrar_usuario(self):

sapo = BaseDeDatos("prueba")
sapo.actualizar_usuario()

#id, Apellido, Nombre, Edad, Correo