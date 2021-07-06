import random as rand 
import arquivos as arq

### Calculos para as redes do espaço neutral ###

## confere se as linhas possuem apenas uma diferença ##

def distanciaHamming(linha_matriz, linha_possivel):

	a = 0
	for i in range(0, len(linha_matriz)):

		if linha_matriz[i] != linha_possivel[i]:
			a += 1

	return a == 1



### Trabalhar com as redes em forma de strings ###

def stringfica_rede(mtz):

	aux = []
	for i in range(0, len(mtz)):

		linhas_possiveis = arq.abre_arquivo_yeast(f'gene{i}')

		for j in range(0, len(linhas_possiveis)):

			if linhas_possiveis[j] == mtz[i]:
				aux.append(j)
				break

	return '-'.join(str(x) for x in aux)

def matriz_da_string(string):

	aux = [int(x) for x in string.split('-')]
	matriz = []
	for i in range(0, 11):
		linhas = arq.abre_arquivo_yeast(f'gene{i}')
		linha = linhas[aux[i]]
		matriz.append(linha)

	return matriz

### Random Heaps ###

def sorteia_descendentes(raiz, nohs):

	linhas_raiz = [int(x) for x in raiz.split('-')]
	desc = []

	while len(desc) < 2:

		gene = rand.randint(0, 10)
		linhas = arq.abre_arquivo_yeast(f'gene{gene}')
		aux = []
		raiz_linha = linhas[linhas_raiz[gene]]
		
		for i in range(0, len(linhas)):

			if distanciaHamming(linhas[i], raiz_linha):
				aux.append(i)

		n = rand.randint(0, len(aux) - 1)
		novo_desc = linhas_raiz.copy()
		novo_desc[gene] = aux[n]

		if novo_desc not in desc and novo_desc not in nohs:
			desc.append('-'.join(str(x) for x in novo_desc))

	return desc 

	
def gera_random_heap(mtz, n):

	raiz = stringfica_rede(mtz)
	nohs = [raiz]
	k = 0
	total = (2**(n+1)) + 1
	while total > 0:

		if  len(nohs) < 2*k + 2:
			nohs += [0] * (2 * len(nohs))
		desc = sorteia_descendentes(raiz, nohs)
		a = desc[0]
		b = desc[1]
		nohs[2*k + 1] = a
		nohs[2*k + 2] = b

		k += 1
		raiz = nohs[k]

		total -= 1


	return nohs


def combina_caminhos(caminho1, caminho2):

	novo_caminho = caminho1

	for i in range(0, len(caminho2)):

		if caminho2[i] not in novo_caminho:
			novo_caminho.append(caminho2[i])

	return novo_caminho