# Usando docstrings para documentar métodos


def minha_funcao(arg1, arg2=None):
    """Minha Função que faz um print dos argumentos passados

    Params:
        arg1:primeiro argumento.
        arg2:segundo argumento, Default: None.
    """
    # Isso é uma forma de documentar o código.
    print(arg1, arg2)


def main():
    print(minha_funcao.__doc__)


if __name__ == "__main__":
    main()
