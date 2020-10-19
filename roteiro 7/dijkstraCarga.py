def dijkstra(vertices, arestas, u, v):
    beta = {}
    phi = {}
    pi = {}

    for i in range(len(vertices)):
        beta[vertices[i]] = float('inf')
        phi[vertices[i]] = 0
        pi[vertices[i]] = 0

    verificacao = 0

    beta[u] = 0
    phi[u] = 1
    pi[u] = "-"
    w = u

    while (w != v):

        verificacao_2 = 0

        for j in arestas:
            if (j[0] == w):
                if phi[j[2]] == 0 and beta[j[2]] > beta[w] + 1:
                    beta[j[2]] = beta[w] + 1
                    pi[j[2]] = w
                    verificacao_2 += 1

        min_beta = float('inf')

        for k in vertices:
            if phi[k] == 0 and beta[k] < float('inf'):
                if beta[k] < min_beta:
                    min_beta = beta[k]

        if verificacao_2 == 0 and min_beta == float('inf'):
            verificacao += 1
            break

        for l in vertices:
            if beta[l] == min_beta and phi[l] == 0 and beta[l] < float('inf'):
                phi[l] = 1
                w = l
                break

    if verificacao == 1:
        return False

    else:
        atual = v
        lista = []

        while atual != u:
            for m in pi:
                if m == atual:
                    lista.append(atual)
                    atual = pi[atual]
                    break

        lista.append(atual)

        return len(lista) - 1, lista[::-1]

def DijkstraCarga(vertices, arestas, u, v, carga, recarga):

    comeco = u
    recarga.insert(0, u)
    recarga.append(v)

    possibilidades = {}

    for i in range(len(recarga)):
        for j in range(len(recarga)):

            if u == recarga[j] or dijkstra(vertices, arestas, u, recarga[j]) == False:
                continue

            caminho = dijkstra(vertices, arestas, u, recarga[j])[0]

            if caminho <= carga:
                possibilidades[u + "-" + recarga[j]] = caminho
        u = recarga[i]
        if i > 0:
            carga = 5

    lista = dijkstra(recarga, possibilidades, comeco, v)

    if lista == False:

        return "Não há caminho !"

    caminho_2 = []
    caminho_final = []

    for i in range(len(lista[1])-1):
        caminho_2.append(dijkstra(vertices, arestas, lista[1][i], lista[1][i+1])[1])

    for i in range(len(caminho_2)):
        for j in range(len(caminho_2[i])):
            if (caminho_2[i][j] not in caminho_final):
                caminho_final.append(caminho_2[i][j])

    return caminho_final