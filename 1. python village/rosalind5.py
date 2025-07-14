f = open(r"C:\Users\anama\Desktop\bioinf\python\python-bioinfo\python village\rosalind_ini5.txt", "r")
lineas = f.readlines()
# i da el valor empezando desde 1, linea aporta la posición de la línea real (1 a la linea 0)
for i, line in enumerate(lineas, start=1):
    if i % 2 == 0:  # líneas pares
        print(line.strip())
