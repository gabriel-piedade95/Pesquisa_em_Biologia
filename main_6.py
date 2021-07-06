import arquivos as arq
import analises as A
import matplotlib.pyplot as plt 

tabela = A.abre_analise('analise_heap_g')

h = tabela['H']
w = tabela['W']


H_wt = h[0]
W_wt = w[0]


plt.title("Convergência x Entropia - Random Heap")
plt.xlabel('Entropia (H)')
plt.ylabel('Convergência (W)')
plt.scatter(h, w, c = 'b', label = 'redes conectadas')
plt.scatter(H_wt, W_wt, c = 'r', label = 'Wildtype')
plt.legend()
plt.show()



