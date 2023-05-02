import os

for i in range (0,4):
    try:
        os.mkdir(f'notas/dir{i}')
        print("Directorios creados")
        with open(f"notas/dir{i}/notas{i}.txt", "wt") as f:
            f.writelines("Hoy es martes, día 2 de mayo de 2023. ")
            f.writelines(f"Esta es la nota {i}.")
    except: 
        print("Directorios ya existen")
        FileExistsError

with open("notas/dir2/notas2.txt", "rt") as f:
    datos = f.read()
    f.close
    print(datos)

with open(f"notas/dir{i}/notas{i}.txt", "at") as f:
    f.write(f"\nHe añadido más texto a las notas con índice {i}")






