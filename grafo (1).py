class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):

        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    '''
    Questao 1 - Encontre todos os pares de vértices não adjacentes.
    '''

    def vertices_nao_adjacentes(self):
        vertices = self.N
        arestas = self.A.values()   # Se colocar só o ".A" ele vai pegar apenas as chaves do dicionário
        nao_adjacentes = []
        for i in vertices:
            for j in vertices:
                verificar_indo = "{}-{}" .format(i, j)
                verificar_vindo = "{}-{}" .format(j, i)
                if verificar_indo not in arestas and verificar_vindo not in arestas:
                    nao_adjacentes.append(verificar_indo)
        return nao_adjacentes

    '''
    Questão 2 - Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
    '''

    def ha_laco(self):
        lista_arestas = self.A.values() #Ao inves de criar uma nova lista, outa forma seria no "FOR" colocar "self.A.values():"
        for i in lista_arestas:
            v1, v2 = i.split(self.SEPARADOR_ARESTA)
            if v1 == v2:
                return True
        return False

    '''
    Questão 3 - Há arestas paralelas? (Retorne True ou False)
    '''
    def ha_paralelas(self):
        arestas = list(self.A.values())

        saida = False

        while len(arestas) >= 1:
            aux = arestas.pop(0)
            if (aux[0] + self.SEPARADOR_ARESTA + aux[2]) in arestas or (aux[2] + self.SEPARADOR_ARESTA + aux[0]) in arestas:
                print(aux[0], aux[2])
                saida = True
                break

        return saida

    '''
    Questão 4 - Qual o grau de um vértice arbitrário?
    '''

    def grau(self, vertice):                        #quantidade de arestas que incidem num vertice
         if self.existeVertice(vertice):
            grau = 0
            for i in self.A:
                if vertice in self.A[i]:
                    grau += 1
            return grau

    '''
    Questão 5 - Quais arestas incidem sobre um vértice N arbitrário?
    '''

    def arestas_sobre_vertice(self, vertice):
        arestas = []
        for i in self.A:  #Chaves do dicionario
            if (vertice in self.A[i]):  #Valores correspondentes a cada chave
                arestas.append(i)
        return arestas

    '''
    Questao 6 - Esse grafo é completo?
    '''
    def eh_completo(self):

        l_vertices = self.N
        l_arestas = list(self.A.values())

        for i in range(len(l_arestas)):
            l_arestas[i] = l_arestas[i].split("-")

        for i in range(len(l_vertices)):
            l = ["", ""]
            for y in range(len(l_vertices) - 1 - i):
                if (l_vertices[i] != l_vertices[y + 1 + i]):
                    l[0] = l_vertices[i]
                    l[1] = l_vertices[y + 1 + i]
                if (l not in l_arestas):
                    l.reverse()
                    if (l not in l_arestas):
                        return False
        return True

    '''
    Roteiro 2 - 
    
    '''
    def  criando_dfs(self, raiz, lista_dfs =[]):
        '''
        :param raiz: vértice que será usado como raiz da DFS
        :param lista_dfs:  lista onde vai ser armazenado os vértices e arestas da dfs.
        :return: Uma lista que indica a ordem de como os vértices e arestas foram percorridos.
        '''

        for i in self.A:                #i = chave de cada valor do dicionário conforme vai iterando
            if raiz == self.A[i][0]:     #Verifica o primeiro vertice da aresta/chave que foi selecionada. Exemplo: 'J-C' (self.A[i][0] == J)
                if raiz not in lista_dfs: #Verifica se o vértice já foi adicionado a lista dfs
                    lista_dfs.append(raiz) #Adiciona caso  não tenha sido

                if self.A[i][2] not in lista_dfs: #Verifica o vertice adjancente ao que foi adicionado se ele já está na lista.Exemplo: J-C (self.A[i][2] == C)
                    lista_dfs.append(i)           #Adiciona a chave/aresta na lista dfs, Exemplo: a1': 'J-C'. Vai ser adicionado 'a1' na lista dfs
                    lista_dfs.append(self.A[i][2]) #Adiciona o vertice adjacente. Exemplo: J-C. Vai ser adicionado 'C'

                    self.criando_dfs(self.A[i][2]) #Passa a nova raiz e chama a função novamente.
                                                 # Seguindo lógica dos comentário, ia passar 'C' como raiz e continuar a busca até todos os vertices serem visitados

            else:                               #Caso a raiz passada não seja igual a self.A[i][0], vai verificar o adjacente  Exemplo: 'E-C' e a raiz passada foi 'C'
                                                #como C!=E deve verificar também o vertice adjancente no caso  self.A[i][2]) séria igual a C e faz o mesmo passo dos comentários anteriores,
                                                #caso não seja vai verificar outra aresta
                if (raiz == self.A[i][2]):
                    if raiz not in lista_dfs:
                        lista_dfs.append(raiz)

                    if self.A[i][0] not in lista_dfs:
                        lista_dfs.append(i)
                        lista_dfs.append(self.A[i][0])

                        self.criando_dfs(self.A[i][0])

        return lista_dfs



    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str


