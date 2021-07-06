import arquivos as arq 
import transicao_estados as tE 
import networkx  as nx 
import matplotlib.pyplot as plt



mtz_wt = arq.dados_wildtype('matriz_wildtype')
transicoes_wt = tE.gera_transicoes(mtz_wt)
lista_transicoes_wt = tE.lista_adjacencia(transicoes_wt)
transicoes_binario_wt = tE.lista_para_binario(lista_transicoes_wt)


G = nx.DiGraph()
G.add_edges_from(transicoes_binario_wt)
plt.figure(2, figsize = (14, 10))
pos = nx.spring_layout(G, k = 0.05)
nx.draw_networkx_nodes(G, pos, node_size = 10, node_color = 'g')
nx.draw_networkx_edges(G, pos, arrows = True)
plt.show()