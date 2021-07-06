import arquivos as arq 
import calculos_estados as cE 
import calculos_redes as cR 
import transicao_estados as tE 
import csv
import pandas as pd 
import networkx as nx 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import numpy as np


def relacoes_entre_genes(gene):

	linhas = arq.abre_arquivo_yeast(f'gene{gene}')
	inibicao = [0] * 11
	nada = [0] * 11
	ativacao = [0] * 11
	
	for i in range(0, len(linhas)):

		for j in range(0, len(linhas[i])):

			if linhas[i][j] == -1:
				inibicao[j] += 1

			if linhas[i][j] == 0:
				nada[j] += 1

			if linhas[i][j] == 1:
				ativacao[j] += 1

	return (inibicao, nada, ativacao)

def gera_barplot_gene(gene):

	relacoes = relacoes_entre_genes(gene)
	
	genes = ['Cln3', 'MBF', 'SBF', 'Cln2', 'Cdh1', 'Swi5', 'CdC20', 'Clb5', 'Sic1', 'Clb2', 'Mcm1']

	total = relacoes[0][0] + relacoes[1][0] + relacoes[2][0]
	inib = [x/total for x in relacoes[0]]
	nd = [x/total for x in relacoes[1]]
	atv = [x/total for x in relacoes[2]] 

	inibicao = plt.bar(genes, inib, width = 0.5, color = 'r', label = 'inibição')
	nada = plt.bar(genes, nd, width = 0.5, color = 'b', bottom = inib, label = 'sem conexão')
	ativacao = plt.bar(genes, atv, width = 0.5, color = 'g', bottom = np.array(inib) + np.array(nd), label = 'ativação')
	plt.title(f'{genes[gene]}')
	plt.show()

### Analise das amostras do componente conexo ###

def gera_analise(arquivo, nome):

	amostras = arq.le_arquivo(arquivo)
	tam = len(amostras)

	mtz_wt = cR.matriz_da_string(amostras[0])
	transicoes_wt = tE.gera_transicoes(mtz_wt)
	lista_wt = tE.lista_adjacencia(transicoes_wt)
	bacias_wt = cE.bacias(lista_wt)

	H_wt = cE.entropia(bacias_wt)
	W_wt = cE.W_total(lista_wt)

	ciclos_amostras = [None] * tam 
	atratores_amostras = [None] * tam
	numero_de_bacias_amostras = [None] * tam
	H_amostras = [None] * tam
	W_amostras = [-1] * tam
	Q_amostras = [None] * tam
	dist_amostras = [None] * tam

	for i in range(0, len(amostras)):

		mtz = cR.matriz_da_string(amostras[i])
		transicoes = tE.gera_transicoes(mtz)
		lista = tE.lista_adjacencia(transicoes)
		bacias = cE.bacias(lista)

		if not cE.ciclos(lista):

			ciclos_amostras[i] = False
			numero_de_bacias_amostras[i] = len(bacias)
			atratores_amostras[i] = cE.atratores(bacias)
			H = cE.entropia(bacias)
			W = cE.W_total(lista)
			H_amostras[i] = H
			W_amostras[i] = W

			d = 0

			for j in range(0, 11):

				for k in range(0, 11):

					if mtz[j][k] != mtz_wt[j][k]:

						d += 1

			dist_amostras[i] = d

		else:

			ciclos_amostras[i] = True

	w = W_wt/max(W_amostras)
	W_amostras = [x/max(W_amostras) if x != -1 else None for x in W_amostras]
	
	for j in range(0, len(amostras)):
		
		if W_amostras[j] != None:
			Q_amostras[j] = cE.dist_Q(H_wt, w, H_amostras[j], W_amostras[j])


	with open(f'/home/gpsp95/Documentos/bio_sist_2/resultados/{nome}.csv', 'w', newline = '', encoding = 'utf-8') as f:

		w = csv.writer(f)
		w.writerow(["Amostra", "Ciclos", "N Bacias", "Atratores", "H", "W", "Q", "dist"])
		
		for l in range(0, tam):

			w.writerow([amostras[l], ciclos_amostras[l], numero_de_bacias_amostras[l], 
				atratores_amostras[l], H_amostras[l], W_amostras[l], Q_amostras[l], dist_amostras[l]])


def abre_analise(nome):

	arquivo_path = f'/home/gpsp95/Documentos/bio_sist_2/resultados/{nome}.csv'
	tabela = pd.read_csv(arquivo_path)

	return tabela


def tds_arestas(nohs):

	arestas = []
	for i in range(0, len(nohs)):
		if nohs[i] != None:
			mtz1 = cR.matriz_da_string(nohs[i])

			for j in range(i + 1, len(nohs)):

				if nohs[j] != None:
					mtz2 = cR.matriz_da_string(nohs[j])
					d = 0
					for k in range(0, 11):

						if cR.distanciaHamming(mtz1[k], mtz2[k]):
							d +=1

					if d == 1:
						arestas.append((nohs[i], nohs[j]))

	return arestas 


def cores_nohs(tabela):

	dic ={}
	
	valores = []
	dic['redes'] = []
	dic['Q'] = []
	lista = tabela['Amostra']
	for i in range(0, len(lista)):

		if  tabela['Amostra'][i] != None:
			val_Q = tabela.loc[tabela['Amostra'] == lista[i], ['Q']].values[0][0]
			valores.append(int(1000 * val_Q))
			dic['redes'].append(lista[i])
			dic['Q'].append(val_Q)

	dic['cores'] = pd.cut(valores, 15, labels = [x for x in range(1, 16)])
	dic = pd.DataFrame(dic)

	return dic 


