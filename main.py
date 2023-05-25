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

    def extraer_datos(self):
        datos = []
        with open(self.path,"r") as file:
            datos = list(csv.reader(file, skipinitialspace=True))
        return datos

    #def actualizar_usuario(self):
       

    #def borrar_usuario(self):
        
    #def borrar_usuario(self):

sapo = BaseDeDatos("prueba")
print(sapo.extraer_datos())

#id, Apellido, Nombre, Edad, Correo