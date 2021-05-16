import struct
from numbers import Number

import numpy as np


class MathUtil:

    @staticmethod
    def flip_bit(bitfield: np.ndarray, pos: int) -> np.ndarray:
        if bitfield[pos] == 0:
            bitfield[pos] = 1
        else:
            bitfield[pos] = 0
        return bitfield

    @staticmethod
    def float_to_bitfield(number: float) -> np.ndarray:
        bits = MathUtil.__float_to_bits(number)
        return MathUtil.__bits_to_bitfield(bits)

    @staticmethod
    def bitfield_to_float(bitfield: np.ndarray) -> float:
        bits = MathUtil.__bitfield_to_bits(bitfield)
        return MathUtil.__bits_to_float(bits)

    @classmethod
    def __float_to_bits(cls, number: float) -> int:
        s = struct.pack('>f', number)
        return struct.unpack('>l', s)[0]

    @classmethod
    def __bits_to_float(cls, bits: Number) -> float:
        s = struct.pack('>l', bits)
        return struct.unpack('>f', s)[0]

    @classmethod
    def __bits_to_bitfield(cls, bits: int) -> np.ndarray:
        # [2:] to chop off the "0b" part
        return np.array([int(digit) for digit in bin(bits)[2:]])

    @classmethod
    def __bitfield_to_bits(cls, bitfield: np.ndarray) -> int:
        out = 0
        for bit in bitfield:
            out = (out << 1) | bit
        return out
