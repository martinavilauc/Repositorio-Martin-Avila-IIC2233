from personalidades import Cascarrabias, Alegre, Presumida
from regalo import Regalo


class Cyrano(Cascarrabias):
    """
    Aldeano cascarrabias.
    ESTE ES EL EJEMPLO RESUELTO: usalo como modelo para los demas
    """

    def __init__(self) -> None:
        """
        Llama a super init para inicializar la clase padre
        """
        super().__init__(nombre="Cyrano", especie="oso hormiguero")


class Rosie(Alegre):
    """
    Aldeana alegre.
    """

    def __init__(self) -> None:
        # POR COMPLETAR (Parte 2)
        super().__init__(nombre="Rosie", especie="gato")


class Peanut(Alegre):
    """
    Aldeana alegre
    """

    def __init__(self) -> None:
        # POR COMPLETAR (Parte 2)
        super().__init__(nombre="Peanut", especie="ardilla")


class Whitney(Presumida):
    """
    Aldeana presumida
    """

    def __init__(self) -> None:
        # POR COMPLETAR (Parte 2)
        super().__init__(nombre="Whitney", especie="lobo")


class TomNook(Cascarrabias):
    """
    Aldeano cascarrabias
    """

    def __init__(self) -> None:
        # POR COMPLETAR (Parte 2)
        super().__init__(nombre="Tom Nook", especie="mapache")


class Canela(Alegre):
    """
    Aldeana alegre
    """

    def __init__(self) -> None:
        # POR COMPLETAR (Parte 2)
        super().__init__(nombre="Canela", especie="perro")
