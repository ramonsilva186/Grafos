from grafo_adj_nao_dir import Grafos

x = Grafos(['A', 'B', 'C', 'D'])

x.adicionaAresta('A-B')
x.adicionaAresta('B-C')
x.adicionaAresta('C-D')
x.adicionaAresta('D-A')



a = x.grau('A')
b = x.grau('B')
c = x.grau('C')
d = x.grau('D')


e = [a, b, c, d]

print(e)
print(x.eh_euleriano())
print(x.caminho_euleriano())