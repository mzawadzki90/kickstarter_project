from typing import TypeVar, Generic

T = TypeVar('T', int, float)


class Gene(Generic[T]):
    label: str
    minimum: T
    maximum: T
    value: T

    def __init__(self, label: str, minimum: T, maximum: T, value: T) -> None:
        self.value = value
        self.label = label
        self.minimum = minimum
        self.maximum = maximum

    def get_type(self) -> type:
        pass


class IntegerGene(Gene[int]):

    def __init__(self, label: str, minimum: int, maximum: int, value: int = 0) -> None:
        super().__init__(label, minimum, maximum, value)

    def get_type(self) -> type:
        return int.__class__


class FloatGene(Gene[float]):

    def __init__(self, label: str, minimum: float, maximum: float, value: float = 0.0) -> None:
        super().__init__(label, minimum, maximum, value)

    def get_type(self) -> type:
        return float.__class__
