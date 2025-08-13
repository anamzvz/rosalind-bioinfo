secuencias = {}
secuencia = None
id = 0
GC_total = []

ruta = "C:\\Users\\anama\\Desktop\\bioinf\\python\\python-bioinfo\\2. bioinformatics stronghold\\datasets\\rosalind_gc.txt"
with open(ruta, "r") as f:
    for linea in f:
        linea = linea.strip()
        if linea.startswith(">"):
            id = linea[1:]
            secuencias[id] = ""
        else:
            secuencias[id] += linea


GC_id = {}
for id_Seq, secuencia in secuencias.items():
    contador_G = 0
    contador_C = 0
    total_nt = len(secuencia)
    for base in secuencia:
        if base == "G":
            contador_G += 1
        if base == "C":
            contador_C += 1
    GC = ((contador_C + contador_G)/(total_nt)) * 100
    GC_id[id_Seq] = GC

max_id = max(GC_id, key=GC_id.get)
print(max_id)
print(GC_id[max_id])
