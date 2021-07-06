import analises as A 
import arquivos as arq 
import calculos_redes as cR 
import csv

mtz_wt = arq.dados_wildtype('matriz_wildtype')

heap = cR.gera_random_heap(mtz_wt, 6)
arq.imprime_heap(heap, 'heap_g')

A.gera_analise(f'heap_g', f'analise_heap_g')

tabela = A.abre_analise('analise_heap_g')

lista = []

for i in range(0, len(tabela)):

	if tabela['Ciclos'][i] == False:
		lista.append(tabela['Amostra'][i])

	else:
		lista.append(None)

arestas = A.tds_arestas(lista)

with open('/home/gpsp95/Documentos/bio_sist_2/resultados/tcc/arestas_heap_g.csv', 'w', newline = '', encoding = 'utf-8') as f:

		w = csv.writer(f)
		w.writerow(["a", "b"])
		
		for l in range(0, len(arestas)):

			w.writerow([arestas[l][0], arestas[l][1]])