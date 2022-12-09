from simplejson import JSONEncoderForHTML
from particula import Particula
from algoritmos import distacia_euclidiana
import json
class Admin:
    def __init__(self):
        self. __almacen=[]


    def agregar_final(self, particula:Particula):
        self. __almacen.append(particula)

    def agregar_inicio(self, particula:Particula):
        self. __almacen.insert(0, particula)
    
    def mostrar(self):
        for particula in self.__almacen:
            print(particula)   

    def __str__(self):
        return "".join(
            str(admin)+ "\n" for admin in self.__almacen )

    def __len__(self):
        return len(self.__almacen)

    def __iter__(self):
        self.cont=0
        return self

    def __next__(self):
        if self.cont< len(self.__almacen):
            Particula=self.__almacen[self.cont]
            self.cont +=1
            return Particula
        else:
            raise StopIteration

    def save(self, ubicacion):
        try:

            with open(ubicacion, 'w') as archivo:
                # archivo.write(str(self))
                lista= [Particula.to_dict() for Particula in self.__almacen]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def open(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista=json.load(archivo)
                self.__almacen=[Particula(**Particula) for Particula in lista ]
            return 1
        except:
            return 0 
    def orde(self):
        self.__almacen.sort()

    def __lt__(self, other):
        id=Particula.id
        return self.id < other.id
        
        




#p01=Particula(id=1,origen_x=10, origen_y=23,destino_x=10,destino_y=1,velocidad=20,red="Rojo",green="Verde", blue="azul",distancia=distacia_euclidiana)
#p02=Particula(2,3,4,5,6,7,"color", "color","color", distacia_euclidiana)
#particula=Admin()
#particula.agregar_final(p01)
#particula.agregar_inicio(p02)
#particula.agregar_inicio(p01)
#particula.mostrar()