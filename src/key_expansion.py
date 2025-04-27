# Key expansion functions for Mini-AES

from src.utils import rotate_nibble, sub_nibbles

def key_expansion(key):
    # Key adalah 16-bit integer
    w = [0] * 6

    w[0] = (key >> 8) & 0xFF  # 8 bit pertama
    w[1] = key & 0xFF         # 8 bit kedua

    # Constants Rcon untuk 4-bit
    Rcon1 = 0x80  # 1000 0000
    Rcon2 = 0x30  # 0011 0000

    # Proses expand
    w[2] = w[0] ^ Rcon1 ^ sub_nibbles(rotate_nibble(w[1]))
    w[3] = w[2] ^ w[1]
    w[4] = w[2] ^ Rcon2 ^ sub_nibbles(rotate_nibble(w[3]))
    w[5] = w[4] ^ w[3]

    # Round keys
    round_keys = [
        (w[0] << 8) | w[1],
        (w[2] << 8) | w[3],
        (w[4] << 8) | w[5],
        ((w[4] << 8) | w[5])  # Duplicate last round key for final round
    ]

    return round_keys
