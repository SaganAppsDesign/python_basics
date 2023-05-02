import os

def greeting():
    nombre = input("Por favor, introduce tu nombre: ")
    print("Hola, ¿qué tal? " + nombre + "\n")
    return nombre

def bbddPlanetLoop(list):
    for i, v in enumerate(list):
            print(str(i + 1) + ". " + v.title())    

planetas = ["mercurio","venus","tierra","marte","jupiter"]

def addPlanets (list):
    respuesta = "si"
    nombre = greeting()
    print("Ahora existe esta BBDD de planetas: \n")
    bbddPlanetLoop(list)
    
    while (respuesta == "si"):
       
        planet = input("\nPor favor, introduce nuevo planeta: ")
        list.append(planet)
        os.system('cls')
        print("Este es el nuevo listado de planetas: \n")
        bbddPlanetLoop(list)
       
        print("\n¿Quieres añadir más planetas?\n")
        respuesta = input().lower()

        if (respuesta == "no"):
            print("\nGracias por su colaboración en nuestra BBDD planetaria " + nombre + "\n")
    
    
addPlanets(planetas)



          
          
        
    

