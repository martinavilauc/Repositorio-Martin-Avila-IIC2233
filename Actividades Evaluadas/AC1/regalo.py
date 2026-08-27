PRECIO_MAXIMO = 500000


class Regalo:
    """
    Clase que modela un objeto que se le puede regalar a un aldeano
    """

    def __init__(self, nombre: str, categoria: str, precio: int) -> None:
        # (Parte 1.1):
        self.nombre = nombre
        self.categoria = categoria
        self._precio = precio

    # (Parte 1.2):

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio_nuevo):
        if 0 <= precio_nuevo <= PRECIO_MAXIMO:
            self._precio = precio_nuevo
        else:
            print(
                f"[Aviso] {precio_nuevo} no es un precio valido (0 a {PRECIO_MAXIMO}). \
                \nSe mantiene {self._precio}."
                )

    # (Parte 1.3):

    def __str__(self):
        return f"{self.nombre} ({self._precio})"

    def __repr__(self):
        return f"Regalo(nombre='{self.nombre}', categoria='{self.categoria}', precio={self._precio})"
