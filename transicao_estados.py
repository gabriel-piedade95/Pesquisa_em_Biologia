
### Funções usadas para encontrar as transições de estados do ciclo celular ###

## O código de Gray é uma sequencia binária em que cada estado tem apenas uma alteração ##
## em relação ao estado anterior. Com isso os calculos se tornam mais faceis###

def codigo_gray(n):
  
  def codigo_gray_str(n):
    
    if n == 0:
      return ['']

    cod_1 = codigo_gray_str(n-1)
    cod_2 = cod_1[::-1].copy()

    for i in range(len(cod_1)):
      cod_1[i] = '0' + cod_1[i]
      
    for j in range(len(cod_2)):
      cod_2[j] = '1' + cod_2[j]
    
    return cod_1 + cod_2

  return [[int(x) for x in lista] for lista in codigo_gray_str(n)]



def gera_transicoes(mtz):

  estados = codigo_gray(11)
  
  transicoes = [(estados[0], estados[0])]


  for i in range(1, len(estados)):
    
    est_ant = transicoes[i - 1][0].copy()
    prox_est = estados[i].copy()
    trn = transicoes[i - 1][1].copy()
    pos = 0

    for n in range(0, len(est_ant)):
      if est_ant[n] != prox_est[n]:
        pos = n
        break

    a = int(est_ant[pos])
    b = int(prox_est[pos])

    if (b - a) != 0:
      for j in range(0, len(mtz)):
        if mtz[j][pos] != 0:
          trn[j] = trn[j] + (mtz[j][pos] * (b - a))

    transicoes.append((prox_est, trn))

  return transicoes


def lista_adjacencia(trns, tam = 11):

  transicoes = [0] * 2048

  for i in range(0, len(trns)):

    aux = [0] * tam

    for j in range(0, len(trns[0][1])):

      if trns[i][1][j] > 0:
        aux[j] = 1

      if trns[i][1][j] < 0:
        aux[j] = 0

      if trns[i][1][j] == 0:
        aux[j] = trns[i][0][j]

    num = ''.join(str(x) for x in aux)
    pos = ''.join(str(x) for x in trns[i][0])

    transicoes[int(pos, 2)] = int(num, 2)
  
  return transicoes

def lista_para_binario(lista, tam = 11):

  trns_bin = []
  for i in range(0, len(lista)):
    ant = '0' * (tam - len(bin(i)[2:])) + bin(i)[2:]
    prox = '0' * (tam - len(bin(lista[i])[2:])) + bin(lista[i])[2:]
    trns_bin.append((ant, prox))

  return trns_bin

def altera_transicoes(mtz, linha, gene, trns):

  n_trns = []

  for trn in trns:

    est_ant = trn[0].copy()
    novo_est = trn[1].copy()
    a = 0
    b = 0
    pos = 0

    for i in range(0, len(linha)):
      if mtz[gene][i] != linha[i]:
        a = mtz[gene][i]
        b = linha[i]
        pos = i
        break

    if (b - a) != 0 and est_ant[pos] != 0:
      novo_est[gene] = novo_est[gene] + (est_ant[pos] * (b - a))

    n_trns.append((est_ant, novo_est))

  return n_trns