class Node:
    def __init__(self, dado) -> None:
        self.dado = dado
        self.proximo = None

    def __repr__(self) -> str:
        return f"{self.dado} -> {self.proximo}"