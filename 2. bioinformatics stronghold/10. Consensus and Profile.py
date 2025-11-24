secuencias = []
secuencia = ""

with open("rosalind_cons.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        if linea.startswith(">"):
            if secuencia != "":
                secuencias.append(secuencia)
                secuencia = ""
        else:
            secuencia += linea
    if secuencia != "":
        secuencias.append(secuencia)

A = []
C = []
G = []
T = []

consenso = ""
for columna in zip(*secuencias):
    a = columna.count('A')
    c = columna.count('C')
    g = columna.count('G')
    t = columna.count('T')
    A.append(a)
    C.append(c)
    G.append(g)
    T.append(t)
    dic = {'A': a, 'C': c, 'G': g, 'T': t}
    maximo = max(dic, key=dic.get)
    consenso += maximo

print(consenso)
print("A:", *A)
print("C:", *C)
print("G:", *G)
print("T:", *T)
