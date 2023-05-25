import csv
class BaseDeDatos():
    def __init__(self,file_name):
        self.path = "./archivos/" + file_name
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



    #def crear_usuario(self):

    #def actualizar_usuario(self):

    #def borrar_usuario(self):
        
    #def borrar_usuario(self):


