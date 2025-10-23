with open("rosalind_subs.txt", "r") as f:
    secuencia = f.readlines()
    sec = secuencia[0].strip()
    motif = secuencia[1].strip()
    posiciones = []

for i in range(0, len(sec) - len(motif) + 1):
    sec_fragmento = sec[i:i+len(motif)]
    if sec_fragmento == motif:
        posiciones.append(i+1)

print(posiciones)
