alfabeto = "zabcdefghijklmnopqrstuvwxy0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/`~"


def equivalenteDecimal(caractere):
    return alfabeto.find(caractere)


def equivalenteAlfabetico(numero):
    return alfabeto[numero]


A = [[5, 6], [2, 3]]


# função responsável por pegar o texto a ser encriptado
def inserirFrase():
    texto = str(input("Informe um texto: "))  # padrão de entrada para receber uma string
    texto = texto.replace(" ", "")  # eliminando os espaços em branco do texto

    # caso o texto tenha uma quantidade ímpar de letras, adiciona mais uma letra arbitrária ao final
    if len(texto) % 2 != 0:
        texto += "g"

    return texto


# função responsável por codificar nossa matriz, dependendo da matriz inserida
def cifraHill(texto, chave):
    codigo = ""
    matriz_codificada = []

    valorNumerico = [0, 0]
    valorCodificado = [0, 0]

    for indice in range(0, len(texto)):
        if indice == 0 or indice % 2 == 0:
            valor = equivalenteDecimal(texto[indice])
            valorNumerico[0] = valor

        if indice != 0 and indice % 2 != 0:
            valor = equivalenteDecimal(texto[indice])
            valorNumerico[1] = valor

        if indice != 0 and indice % 2 != 0:
            valorCodificado[0] = chave[0][0] * valorNumerico[0] + chave[0][1] * valorNumerico[1]
            valorCodificado[1] = chave[1][0] * valorNumerico[0] + chave[1][1] * valorNumerico[1]

            if valorCodificado[0] > len(alfabeto) - 1:
                valorCodificado[0] = (valorCodificado[0] % len(alfabeto))

            if valorCodificado[1] > len(alfabeto) - 1:
                valorCodificado[1] = (valorCodificado[1] % len(alfabeto))

            a = str(equivalenteAlfabetico(valorCodificado[0]))
            b = str(equivalenteAlfabetico(valorCodificado[1]))
            codigo += a
            codigo += b

            # Adiciona o par de valores numéricos codificados à matriz
            matriz_codificada.append([valorCodificado[0], valorCodificado[1]])

    # remove os caracteres desnecessários e mostra somente a parte codificada
    codigo = codigo[len(codigo) - len(texto): len(codigo)]

    # Imprime a matriz codificada
    print("Matriz codificada: ", matriz_codificada)

    return codigo


def inversaHill(codigo, chave_inversa):
    matriz_decodificada = []

    valorNumerico = [0, 0]
    valorDecodificado = [0, 0]

    for indice in range(0, len(codigo)):
        if indice == 0 or indice % 2 == 0:
            valor = equivalenteDecimal(codigo[indice])
            valorNumerico[0] = valor

        if indice != 0 and indice % 2 != 0:
            valor = equivalenteDecimal(codigo[indice])
            valorNumerico[1] = valor

        if indice != 0 and indice % 2 != 0:
            valorDecodificado[0] = chave_inversa[0][0] * valorNumerico[0] + chave_inversa[0][1] * valorNumerico[1]
            valorDecodificado[1] = chave_inversa[1][0] * valorNumerico[0] + chave_inversa[1][1] * valorNumerico[1]

            if valorDecodificado[0] > len(alfabeto) - 1:
                valorDecodificado[0] = (valorDecodificado[0] % len(alfabeto))

            if valorDecodificado[1] > len(alfabeto) - 1:
                valorDecodificado[1] = (valorDecodificado[1] % len(alfabeto))

            matriz_decodificada.append([valorDecodificado[0], valorDecodificado[1]])

    return matriz_decodificada


texto = inserirFrase()
codigo = cifraHill(texto, A)
matriz_decodificada = inversaHill(codigo, A)

print("Matriz decodificada: ", matriz_decodificada)
print(codigo)
