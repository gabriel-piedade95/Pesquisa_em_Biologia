import re

### Funções usadas para abrir e gerar arquivos ###


## É necessário preencher o caminho até essa pasta ## 
path = ''

def abre_arquivo_yeast(nome):

  linhas = []

  with open(path + f'genes_yeast/{nome}.txt','r', encoding='utf-8') as f:
    
    for linha in f:
      linhas.append([int(k) for k in re.findall(r'-?\d+', linha)])
    
  return linhas


def dados_wildtype(dado):

	linhas = []

	with open(path + f'dados/{dado}.txt', 'r', encoding = 'utf-8') as f:

		for linha in f:
			linhas.append([int(k) for k in re.findall(r'-?\d+', linha)])
    
	return linhas


def imprime_heap(nohs, nome):

	with open(path + f'resultados/{nome}.txt', 'w', encoding = 'utf-8') as f:
		for l in range(0, len(nohs)):
			if nohs[l] != 0:
				for d in nohs[l]:
					f.write(d)

				f.write('\n')


def le_arquivo(nome):

	linhas = []
	with open(path + f'resultados/{nome}.txt',
	 'r', encoding = 'utf-8') as f:
		for linha in f:
			linhas.append(linha[:-1])

	return linhas