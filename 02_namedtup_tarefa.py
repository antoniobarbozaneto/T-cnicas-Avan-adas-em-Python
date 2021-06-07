# Uso de objetos namedtuple
import collections


def main():
    # TODO: Crie uma namedtuple para armazenar coordenadas
    coordenadas = collections.namedtuple("Coordenadas", "x y z")

    p1 = coordenadas(10, 20, 30)
    p2 = coordenadas(30, 40, 50)
    print(p1, p2)
    print(p1.x, p1.y, p1.z)

    # TODO: Use _replace() para criar uma instância nova
    p1 = p1._replace(x=100)

    print(p1)


if __name__ == "__main__":
    main()
