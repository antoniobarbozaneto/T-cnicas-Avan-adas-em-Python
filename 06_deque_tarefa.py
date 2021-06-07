# Deques são filas duplamente terminadas
import collections
import string


def main():
    # TODO: Inicialize um deque com letras minúsculas
    letrinhas = collections.deque(string.ascii_lowercase)

    # TODO: Deques suportam o método len(), mostre o tamanho da deque
    print(len(letrinhas))

    # TODO: Itere sobre a deque criada
    # for letra in letrinhas:
    #    print(letra.upper(), end=',')

    # TODO: Manipule os itens em qualquer um dos terminais
    letrinhas.pop()  # remove o que está na primeira posição
    letrinhas.popleft()  # remove remove o que está na última posição
    letrinhas.append(2)  # adiciona na primeira posição
    letrinhas.appendleft(1)  # aidiciona na última posição
    print(letrinhas)

    # TODO: Rotacione a deque
    print(letrinhas)
    letrinhas.rotate(10)
    print(letrinhas)


if __name__ == "__main__":
    main()
