from __future__ import annotations
from abc import ABC, abstractmethod


class Guerrero:
    pass

class Inicio():
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Estado inicial: {self._state}")

    def fusionar(self) -> None:
        print("Ahora somos Vegito.")
        self._state = 'Vegito'


    def estado(self) -> Guerrero:
        return Tiempo(self._state)

    def perder(self, guerrero: Guerrero) -> None:
        self._state = guerrero.get_state()
        print(f"Perdiendo fusion: {self._state}")


class fusion(Guerrero):
    pass

class Tiempo(fusion):
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state

class Regreso():

    def __init__(self, inicio: Inicio) -> None:
        self._Desfusionarse = []
        self._inicio = inicio

    def backup(self) -> None:
        self._Desfusionarse.append(self._inicio.estado())

    def undo(self) -> None:
        if not len(self._Desfusionarse):
            return

        guerrero = self._Desfusionarse.pop()
        try:
            self._inicio.perder(guerrero)
        except Exception:
            self.undo()



if __name__ == "__main__":
    inicio = Inicio("Vegeta y Goku.\n")
    regreso = Regreso(inicio)
    inicio.fusionar()
    print("\n30 min despues\n")
    regreso.backup()
    regreso.undo()
