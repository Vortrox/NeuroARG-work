import numpy as np
from mod_inv import mod_mat_inv

default_encoding = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz0123456789")}

class HillCipher:
    @staticmethod
    def key_is_valid(key: np.ndarray):
        # Check if square
        if len(key.shape) != 2 or key.shape[0] != key.shape[1]:
            return False

        # Check if invertible
        return np.linalg.det(key) != 0

    def __init__(self, key: np.ndarray, n_letters: int=-1, char_encoding: dict[str, int]=None):
        if char_encoding is None:
            char_encoding = default_encoding

        if n_letters == -1:
            n_letters = key.size

        HillCipher.key_is_valid(key)
        self.key = key
        self.n = key.shape[0]
        self.n_letters = n_letters
        self.char_encoding = char_encoding

    def encode_text(self, text: str) -> np.ndarray:
        # This only converts text from the string form to matrix form, it does not encrypt
        if len(text) % self.n != 0:
            raise ValueError(f"Input string size must be divisible by {self.n}")

        cols = len(text) // self.n
        encoded_text = np.empty(shape=(self.n, cols), dtype=int)

        for i, c in enumerate(text):
            row = i % self.n
            col = i // self.n
            encoded_text[row, col] = self.char_encoding[c]

        return encoded_text

    def decode_text(self, encoded_text: np.ndarray) -> str:
        # This only converts text from the matrix form to string form, it does not decrypt
        rows, cols = encoded_text.shape
        text = ""

        for row in range(rows):
            for col in range(cols):
                text += encoded_text[row, col]

        return text

    def encrypt(self, plaintext: str) -> str:
        encoded_text = self.encode_text(plaintext)
        encoded_ciphertext = np.mod(self.key @ encoded_text, self.n_letters)
        ciphertext = self.decode_text(encoded_ciphertext)

        return ciphertext

    def decrypt(self, ciphertext: str):
        encoded_ciphertext = self.encode_text(ciphertext)
        inverse_key = mod_mat_inv(self.key, self.n_letters)
        encoded_text = np.mod(inverse_key @ encoded_ciphertext, self.n_letters)
        plaintext = self.decode_text(encoded_text)

        return plaintext
