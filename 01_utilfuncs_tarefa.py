# demonstrate built-in utility functions


def main():
    # TODO: Use any() e all() para testar para valores boleanos
    lista = [1, 2, 3, 4, 5, 6]

    # TODO: A função any vai devolver true caso qualquer valor da lista
    # seja verdade
    print(any(lista))  # Any funciona como o OR

    # TODO: A função all vai devolver true apenas se todos valores da
    # lista forem verdade
    print(all(lista))

    # TODO: As funções min e max devolvem os valores mínimo e máximo
    # respectivamente
    print('Valor mínimo: ', min(lista))
    print("Valor máximo: ", max(lista))

    # TODO: Use sum() para somar todos os valores da lista
    print("Somatório: ", sum(lista))


if __name__ == "__main__":
    main()
