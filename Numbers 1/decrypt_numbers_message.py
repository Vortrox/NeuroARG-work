import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# 1. I can never say oh it’s been so long
def l1(num: int) -> int:
    yield num


# 2. Counting all the days, it’s been so damn long
def l2(num: int) -> int:
    yield num


# 3. Oh how much I’m scared to let you go…
def l3(num: int) -> int:
    yield num


# 4. Somewhere in the walls I hear you talk…
def l4(num: int) -> int:
    yield num


# 5. Finding all these numbers
def l5(num: int) -> int:
    yield num


# 6. Start with number 2 yeah
def l6(num: int) -> int:
    yield 2


# 7. Matching all the letters
def l7(num: int) -> int:
    yield num


# 8. 572943
def l8(num: int) -> int:
    # Add 572943
    yield num + 572943
    # Concat 572943 to front
    yield int(f"{num}572943")
    # Concat 572943 to back
    yield int(f"572943{num}")
    # Remove all digits in 572943 before 2
    yield 2943


# 9. Add another 9 yeah
def l9(num: int) -> int:
    # Add 9
    yield num + 9
    # Concat 9 to front
    yield int(f"{num}9")
    # Concat 9 to back
    yield int(f"9{num}")


# 10. Add another line yeah
def l10(num: int) -> int:
    yield num


# 11. Multiply by 5 yeah
def l11(num: int) -> int:
    yield num * 5


# 12. How long will I keep this up?
def l12(num: int) -> int:
    yield num


# 13. I how much it hurts to see you go…
def l13(num: int) -> int:
    yield num


# 14. Generating lyrics is a pain
def l14(num: int) -> int:
    yield num


# 15. Add another 6 yeah
def l15(num: int) -> int:
    # Add 6
    yield num + 6
    # Concat 6 to front
    yield int(f"{num}6")
    # Concat 6 to back
    yield int(f"6{num}")


# 16. Flip the numbers backwards
def l16(num: int) -> int:
    # Flip the entire sequence of numbers backwards e.g: 123 -> 321
    yield int(str(num)[::-1])


# 17. Make the 2 a 3 yeah
def l17(num: int) -> int:
    # Replace all 2s in the sequence with 3
    yield int(str(num).replace("2", "3"))


# 18. Abcdefg
def l18(num: int) -> int:
    yield num


# 19. Multiply by 9 yeah
def l19(num: int) -> int:
    yield num * 9


# 20. Add the numbers 2 4
def l20(num: int) -> int:
    # Add 2 then add 4
    yield num + 2 + 4
    # Concat 24 to front
    yield int(f"{num}24")
    # Concat 24 to back
    yield int(f"24{num}")


# 21. 17 is first yeah
def l21(num: int) -> int:
    # Concat 17 to front
    yield int(f"17{num}")

    # Remove all digits before the first "17" in the sequence. Remove the sequence if there is no "17"
    num_str = str(num)
    if "17" not in num_str:
        yield None
    else:
        num_str = num_str[num_str.find("17"):]
        yield int(num_str)


# 22. Abcdefg
def l22(num: int) -> int:
    yield num


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


if __name__ == "__main__":
    line_functions = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21,
                      l22]
    numbers = {0}
    for func in line_functions:
        new_numbers = {j for i in numbers for j in func(i) if j is not None}
        numbers = new_numbers

    print(numbers)
    print(*numbers, sep="\n")

    with open("numbers_video_base64.txt", "rb") as fp:
        numbers_video_description = fp.readline()
    base64_bytes = base64.b64encode(numbers_video_description)
    for key in numbers:
        cipher = AESCipher(str(key))
        try:
            decoded_message = cipher.decrypt(base64_bytes)
            print(decoded_message)
        except UnicodeDecodeError:
            pass
