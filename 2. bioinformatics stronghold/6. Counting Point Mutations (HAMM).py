ruta = "C:/Users/anama/Desktop/bioinf/python/python-bioinfo/2. bioinformatics stronghold/datasets/rosalind_hamm.txt"
with open(ruta, "r") as f:
    linea = f.readlines()
    s = linea[0].strip()
    t = linea[1].strip()
    contador = 0

for a, b in zip(s, t):
    if a != b:
        contador += 1
print(contador)
