from bases import Aldeano, Interaccion
from regalo import Regalo

PRECIO_CARO = 5000


class Cascarrabias(Aldeano):
    """
    Aldeanos a los que solo los impresionan los regalos caros
    """

    def __add__(self, regalo: Regalo) -> Interaccion:
        """
        POR COMPLETAR (Parte 3):
        """
        if regalo.precio >= PRECIO_CARO:
            self.amistad += 10
        else:
            self.amistad -= 5


class Alegre(Aldeano):
    """
    Aldeanos que agradecen cualquier regalo, y que se vuelven locos
    con la fruta
    """

    def __add__(self, regalo: Regalo) -> Interaccion:
        """
        POR COMPLETAR (Parte 3)
        """
        if regalo.categoria == "fruta":
            self.amistad += 12
        else:
            self.amistad += 5


class Presumida(Aldeano):
    """
    Aldeanos que solo valoran la ropa, y que ademas exigen que sea cara
    """

    def __add__(self, regalo: Regalo) -> Interaccion:
        """
        POR COMPLETAR (Parte 3)
        """
        if regalo.categoria == "ropa":
            if regalo.precio >= PRECIO_CARO:
                self.amistad += 15
            else:
                self.amistad += 6
        else:
            self.amistad += 1
