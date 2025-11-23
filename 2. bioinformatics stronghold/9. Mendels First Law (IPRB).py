
with open("rosalind_iprb.txt", "r") as f:
    linea = f.read().strip()
    k, m, n = map(int, linea.split())
total = k+m+n
parejas = total * (total-1)
n_n = n*(n-1)*1
n_m = (n*m*2)*0.5
m_m = (m*(m-1))*0.25

prob_het = 1-((n_n+n_m+m_m)/parejas)
print(prob_het)
