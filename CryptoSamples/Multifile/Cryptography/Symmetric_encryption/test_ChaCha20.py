import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

nonce = os.urandom(8)
counter = 0
full_nonce = struct.pack("<Q", counter) + nonce
algorithm = algorithms.ChaCha20(key, full_nonce)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message")
decryptor = cipher.decryptor()
decryptor.update(ct)