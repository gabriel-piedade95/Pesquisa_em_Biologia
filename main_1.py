import arquivos as arq 
import transicao_estados as tE 
import calculos_estados as cE
import pandas as pd


## Gerar as transições dos estados do cliclo celuar da rede Wildtype (wt) ##
mtz_wt = arq.dados_wildtype('matriz_wildtype')
transicoes_wt = tE.gera_transicoes(mtz_wt)
lista_transicoes_wt = tE.lista_adjacencia(transicoes_wt)
transicoes_binario_wt = tE.lista_para_binario(lista_transicoes_wt)
bacias_wt = cE.bacias(lista_transicoes_wt)


## Informações sobre as transições da redes ##
tamanho_bacias_wt = cE.tamanho_bacias(bacias_wt)
atratores_bacias_wt = cE.atratores(bacias_wt)
ciclos_rede_wt = cE.ciclos(lista_transicoes_wt)
entropia_wt = cE.entropia(bacias_wt)
convergencia_wt = cE.W_total(lista_transicoes_wt)

## Imprime os resultados ##
dic1 = {}
dic1['tamanho bacias'] = [] 
dic1['atratores'] = []

for i in range(0, len(tamanho_bacias_wt)):
	dic1['tamanho bacias'].append(tamanho_bacias_wt[i])
	dic1['atratores'].append(atratores_bacias_wt[i])

df = pd.DataFrame(dic1)
print(df)

print('\n\n')

if ciclos_rede_wt:
	r = 'Sim'
else:
	r = 'Não'
print('Existem ciclos: ' + r)

print('\n\n')
print(f'H = {entropia_wt}')
print(f'W = {convergencia_wt}')