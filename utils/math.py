import struct
from numbers import Number

import numpy as np


class MathUtil:

    @staticmethod
    def set_equal_length(arr1: np.ndarray, arr2: np.ndarray) -> [np.ndarray, np.ndarray]:
        if len(arr1) < len(arr2):
            new_arr1 = arr1.copy()
            new_arr1 = new_arr1.resize(arr2.shape)
            new_arr2 = arr2.copy()
        else:
            new_arr2 = arr2.copy()
            new_arr2 = new_arr2.resize(arr1.shape)
            new_arr1 = arr1.copy()
        return new_arr1, new_arr2

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

    @staticmethod
    def integer_to_bitfield(number: int) -> np.ndarray:
        bits = MathUtil.__integer_to_bits(number)
        return MathUtil.__bits_to_bitfield(bits)

    @staticmethod
    def bitfield_to_integer(bitfield: np.ndarray) -> int:
        bits = MathUtil.__bitfield_to_bits(bitfield)
        return MathUtil.__bits_to_integer(bits)

    @classmethod
    def __float_to_bits(cls, number: float) -> int:
        s = struct.pack('>f', number)
        return struct.unpack('>l', s)[0]

    @classmethod
    def __bits_to_float(cls, bits: Number) -> float:
        s = struct.pack('>l', bits)
        return struct.unpack('>f', s)[0]

    @classmethod
    def __integer_to_bits(cls, number: int) -> int:
        s = struct.pack('>i', number)
        return struct.unpack('>l', s)[0]

    @classmethod
    def __bits_to_integer(cls, bits: Number) -> int:
        s = struct.pack('>l', bits)
        return struct.unpack('>i', s)[0]

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
