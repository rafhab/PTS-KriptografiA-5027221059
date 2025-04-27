# S-Box, Inverse S-Box, MixColumns, Inverse MixColumns

# S-Box untuk substitusi nibble
S_BOX = {
    0x0: 0x9, 0x1: 0x4, 0x2: 0xA, 0x3: 0xB,
    0x4: 0xD, 0x5: 0x1, 0x6: 0x8, 0x7: 0x5,
    0x8: 0x6, 0x9: 0x2, 0xA: 0x0, 0xB: 0x3,
    0xC: 0xC, 0xD: 0xE, 0xE: 0xF, 0xF: 0x7
}

# Inverse S-Box
INV_S_BOX = {v: k for k, v in S_BOX.items()}

def sub_nibbles(value):
    high = (value >> 4) & 0xF
    low = value & 0xF
    return (S_BOX[high] << 4) | S_BOX[low]

def inv_sub_nibbles(value):
    high = (value >> 4) & 0xF
    low = value & 0xF
    return (INV_S_BOX[high] << 4) | (INV_S_BOX[low])

def rotate_nibble(value):
    return ((value & 0xF) << 4) | ((value >> 4) & 0xF)

def shift_rows(value):
    n0 = (value >> 12) & 0xF
    n1 = (value >> 8) & 0xF
    n2 = (value >> 4) & 0xF
    n3 = value & 0xF
    return (n0 << 12) | (n3 << 8) | (n2 << 4) | (n1)

def inv_shift_rows(value):
    n0 = (value >> 12) & 0xF
    n1 = (value >> 8) & 0xF
    n2 = (value >> 4) & 0xF
    n3 = value & 0xF
    return (n0 << 12) | (n1 << 8) | (n2 << 4) | (n3)

def mix_columns(value):
    n0 = (value >> 12) & 0xF
    n1 = (value >> 8) & 0xF
    n2 = (value >> 4) & 0xF
    n3 = value & 0xF

    new_n0 = n0 ^ gf_mul(4, n1)
    new_n1 = gf_mul(4, n0) ^ n1
    new_n2 = n2 ^ gf_mul(4, n3)
    new_n3 = gf_mul(4, n2) ^ n3

    return (new_n0 << 12) | (new_n1 << 8) | (new_n2 << 4) | new_n3

def inv_mix_columns(value):
    n0 = (value >> 12) & 0xF
    n1 = (value >> 8) & 0xF
    n2 = (value >> 4) & 0xF
    n3 = value & 0xF

    new_n0 = gf_mul(9, n0) ^ gf_mul(2, n1)
    new_n1 = gf_mul(2, n0) ^ gf_mul(9, n1)
    new_n2 = gf_mul(9, n2) ^ gf_mul(2, n3)
    new_n3 = gf_mul(2, n2) ^ gf_mul(9, n3)

    return (new_n0 << 12) | (new_n1 << 8) | (new_n2 << 4) | new_n3

def gf_mul(x, y):
    # Perkalian dalam GF(2^4) dengan modul x^4 + x + 1
    result = 0
    for i in range(4):
        if (y & 1):
            result ^= x
        high_bit = x & 0x8
        x <<= 1
        if high_bit:
            x ^= 0x13  # x^4 + x + 1 polinomial => 0b10011 = 0x13
        y >>= 1
    return result & 0xF
