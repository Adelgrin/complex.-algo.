#não gostaria de fazer
#eu tbm não
def imprime_vetor_recursivo(vetor, indice=0):
    if indice < len(vetor):
        print(vetor[indice])
        imprime_vetor_recursivo(vetor, indice + 1)

# Exemplo de uso
vetor = [1, 2, 3, 4, 5]
#vetor = ["a", "b", "c", "d", "e"]
imprime_vetor_recursivo(vetor)