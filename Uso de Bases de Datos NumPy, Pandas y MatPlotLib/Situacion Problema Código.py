import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Se importa el archivo de excel
root = "MuertesCOVID-19.xlsx"
df = pd.read_excel(root, skiprows=1)

#se selecciona un número aleatorio como cotraseña
num_aleatorio = int(random.randint(1, 9999))

#Si es menor a 1000 que se pongan 0 de acuerdo con los dígitos que faltan
password = ""
if num_aleatorio < 10:
    password = f"000{num_aleatorio}"
elif num_aleatorio < 100:
    password = f"00{num_aleatorio}"
elif num_aleatorio < 1000:
    password = f"0{num_aleatorio}"
else: password = f"{num_aleatorio}"

# Esta línea imprimirá el valor de password en la consola
contraseña = input(f"La contraseña es: {password} \nIntroduce la contaseña: ")

usando = True

while usando:
    #Si la contraseña es correcta se le lleva al menú
    if contraseña == password:
        opcion = int(input("""
 ___________________________________________________________________________________________________________________
        Escribe el número de la opción que quieras elegír
        1.	¿Cuántos hombres y mujeres difuntos fueron los de la muestra estudiada a causa del COVID-19? 
        2.	¿En qué estado de la República Mexicana hubo más muertes dentro de la muestra de 30 personas? 
        3.	¿Dichas personas contaban con seguro médico? 
        4.	¿Cuánto era lo que ganaban de sueldo dichas personas?
        5.	¿Cuántos años tenían?
        Otro.	Salir
 ___________________________________________________________________________________________________________________       
        """))
        
    #Si no es correcta se repite la pregunta    
    else: contraseña = input(f"Contraseña Incorrecta \nLa contraseña es: {password} \nIntroduce la contaseña: ")

    #Se le lleva a la gráfica de acuerdo con la pregunta seleccionada
    if opcion == 1:
        sexo = df["Sexo"].values.tolist()
        mas = 0
        fem = 0
        i = 0
        while i < len(sexo):
            if sexo[i] == "Masculino":
                mas += 1
            else: fem += 1
            i += 1
        fig, ax = plt.subplots()
        ax.bar(["Hombres", "Mujeres"], [mas, fem])
        plt.title("Número de personas difuntas por sexo")
        plt.xlabel("Sexo")
        plt.ylabel("Cantidad")
        plt.show()
        
    elif opcion == 2:
        estado = df["Estado"].values.tolist()
        estmort = {}
        i = 0
        while i < len(estado):
            if estado[i] not in estmort:
                estmort.setdefault(estado[i],1)
            else: estmort[estado[i]] += 1
            i += 1
        estmort = dict(sorted(estmort.items(), key=lambda x: x[1], reverse=True))
        fig, ax = plt.subplots()
        ax.pie(estmort.values(), labels=estmort.keys(), autopct='%1.1f%%', textprops={'fontsize': 8})
        ax.set_title("Distribución de fallecidos por estado")
        plt.show()
        
    elif opcion == 3:
        seguro = df["Seguro Médico "].values.tolist()
        si = 0
        no = 0
        i = 0
        while i < len(seguro):
            if seguro[i] == "Si":
                si += 1
            else: no += 1
            i += 1
        fig, ax = plt.subplots()
        ax.bar(["Cuentan con seguro", "No cuentan con seguro"], [si, no])
        plt.title("Número de personas difuntas con seguro")
        plt.xlabel("Seguro")
        plt.ylabel("Cantidad")
        plt.show()
        
    elif opcion == 4:
        sueldo = df["Sueldo del individuo "].values.tolist()
        dicsueldo = {"<20,000":0,"20,000-40,000":0,"40,000-60,000":0,"60,000-80,000":0,"80,000-100,000":0,">100,000":0}
        i = 0
        while i < len(sueldo):
            if int(sueldo[i]) < 20000:
                dicsueldo["<20,000"] += 1
            elif int(sueldo[i]) >= 20000 and int(sueldo[i]) < 40000:
                dicsueldo["20,000-40,000"] += 1
            elif int(sueldo[i]) >= 40000 and int(sueldo[i]) < 60000:
                dicsueldo["40,000-60,000"] += 1
            elif int(sueldo[i]) >= 60000 and int(sueldo[i]) < 80000:
                dicsueldo["60,000-80,000"] += 1
            elif int(sueldo[i]) >= 80000 and int(sueldo[i]) < 100000:
                dicsueldo["80,000-100,000"] += 1
            else: dicsueldo[">100,000"] += 1
            i+=1
        fig, ax = plt.subplots()
        ax.bar(list(dicsueldo.keys()), list(dicsueldo.values()))
        plt.title("Número de personas difuntas por rango de sueldo")
        plt.xlabel("Rango de Sueldo")
        plt.ylabel("Cantidad")
        plt.show()
            
    elif opcion == 5:
        edad = df["Edad"].values.tolist()
        dicedad = {"<20":0,"20-30":0,"30-40":0,"40-50":0,"50-60":0,">60":0}
        i = 0
        while i < len(edad):
            if int(edad[i]) < 20:
                dicedad["<20"] += 1
            elif int(edad[i]) >= 20 and int(edad[i]) < 30:
                dicedad["20-30"] += 1
            elif int(edad[i]) >= 30 and int(edad[i]) < 40:
                dicedad["30-40"] += 1
            elif int(edad[i]) >= 40 and int(edad[i]) < 50:
                dicedad["40-50"] += 1
            elif int(edad[i]) >= 50 and int(edad[i]) < 60:
                dicedad["50-60"] += 1
            else: dicedad[">60"] += 1
            i += 1
        fig, ax = plt.subplots()
        ax.bar(list(dicedad.keys()), list(dicedad.values()))
        plt.title("Número de personas difuntas por rango de Edad")
        plt.xlabel("Rango de Edad")
        plt.ylabel("Cantidad")
        plt.show()
        
    else:
        print("Gracias por usar la aplicación")
        usando = False