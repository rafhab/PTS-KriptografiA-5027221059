# Mini-AES encryption and decryption implementation

from src.utils import sub_nibbles, shift_rows, mix_columns, add_round_key
from src.key_expansion import key_expansion

class MiniAES:
    def __init__(self, key):
        self.round_keys = key_expansion(key)

    def encrypt(self, plaintext):
        state = plaintext
        logs = []

        # Round 0: AddRoundKey
        state = add_round_key(state, self.round_keys[0])
        logs.append(("AddRoundKey (Round 0)", state))

        # Round 1
        state = sub_nibbles(state)
        logs.append(("SubNibbles (Round 1)", state))
        state = shift_rows(state)
        logs.append(("ShiftRows (Round 1)", state))
        state = mix_columns(state)
        logs.append(("MixColumns (Round 1)", state))
        state = add_round_key(state, self.round_keys[1])
        logs.append(("AddRoundKey (Round 1)", state))

        # Round 2
        state = sub_nibbles(state)
        logs.append(("SubNibbles (Round 2)", state))
        state = shift_rows(state)
        logs.append(("ShiftRows (Round 2)", state))
        state = mix_columns(state)
        logs.append(("MixColumns (Round 2)", state))
        state = add_round_key(state, self.round_keys[2])
        logs.append(("AddRoundKey (Round 2)", state))

        # Round 3 (Final Round - without MixColumns)
        state = sub_nibbles(state)
        logs.append(("SubNibbles (Round 3)", state))
        state = shift_rows(state)
        logs.append(("ShiftRows (Round 3)", state))
        state = add_round_key(state, self.round_keys[3])
        logs.append(("AddRoundKey (Round 3)", state))

        return state, logs

    def decrypt(self, ciphertext):
        state = ciphertext
        logs = []

        # Round 3 (inverse)
        state = add_round_key(state, self.round_keys[3])
        logs.append(("AddRoundKey (Round 3)", state))
        state = shift_rows(state, inverse=True)
        logs.append(("Inverse ShiftRows (Round 3)", state))
        state = sub_nibbles(state, inverse=True)
        logs.append(("Inverse SubNibbles (Round 3)", state))

        # Round 2 (inverse)
        state = add_round_key(state, self.round_keys[2])
        logs.append(("AddRoundKey (Round 2)", state))
        state = mix_columns(state, inverse=True)
        logs.append(("Inverse MixColumns (Round 2)", state))
        state = shift_rows(state, inverse=True)
        logs.append(("Inverse ShiftRows (Round 2)", state))
        state = sub_nibbles(state, inverse=True)
        logs.append(("Inverse SubNibbles (Round 2)", state))

        # Round 1 (inverse)
        state = add_round_key(state, self.round_keys[1])
        logs.append(("AddRoundKey (Round 1)", state))
        state = mix_columns(state, inverse=True)
        logs.append(("Inverse MixColumns (Round 1)", state))
        state = shift_rows(state, inverse=True)
        logs.append(("Inverse ShiftRows (Round 1)", state))
        state = sub_nibbles(state, inverse=True)
        logs.append(("Inverse SubNibbles (Round 1)", state))

        # Final Round 0
        state = add_round_key(state, self.round_keys[0])
        logs.append(("AddRoundKey (Round 0)", state))

        return state, logs
