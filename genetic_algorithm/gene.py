from typing import TypeVar, Generic

T = TypeVar('T', int, float)


class Gene(Generic[T]):
    value: T
    minimum: T
    maximum: T

    def __init__(self, value: T, minimum: T, maximum: T) -> None:
        self.value = value
        self.minimum = minimum
        self.maximum = maximum


class IntegerGene(Gene[int]):

    def __init__(self, value: int, minimum: int, maximum: int) -> None:
        super().__init__(value, minimum, maximum)


class FloatGene(Gene[float]):

    def __init__(self, value: float, minimum: float, maximum: float) -> None:
        super().__init__(value, minimum, maximum)
