from typing import TypeVar, Generic

T = TypeVar('T', int, float)


class Gene(Generic[T]):
    label: str
    value: T
    minimum: T
    maximum: T

    def __init__(self, label: str, value: T, minimum: T, maximum: T) -> None:
        self.label = label
        self.value = value
        self.minimum = minimum
        self.maximum = maximum

    def get_type(self) -> type:
        pass


class IntegerGene(Gene[int]):

    def __init__(self, label: str, value: int, minimum: int, maximum: int) -> None:
        super().__init__(label, value, minimum, maximum)

    def get_type(self) -> type:
        return int.__class__


class FloatGene(Gene[float]):

    def __init__(self, label: str, value: float, minimum: float, maximum: float) -> None:
        super().__init__(label, value, minimum, maximum)

    def get_type(self) -> type:
        return float.__class__
