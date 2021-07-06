import analises as A
import networkx as nx 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib as mpl

tabela = A.abre_analise('analise_heap_g')
arestas = A.abre_analise('arestas_heap_g')


lista_arestas = [] 
for i in range(0, len(arestas)):
	lista_arestas.append((arestas['a'][i], arestas['b'][i]))


G = nx.Graph()
dic = A.cores_nohs(tabela)

plt.title("Random Heap do Componente conexo")
G.add_nodes_from(dic['redes'][0:])
G.add_edges_from(lista_arestas)
G.add_node(dic['redes'][0])
nx.draw(G, node_color = dic['cores'][:245], edgecolors = ['red']+['black']*244, node_size = 100)
plt.show()