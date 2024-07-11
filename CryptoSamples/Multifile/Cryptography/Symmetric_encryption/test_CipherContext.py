import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
# the buffer needs to be at least len(data) + n - 1 where n is cipher/mode block size in bytes
buf = bytearray(31)
len_encrypted = encryptor.update_into(b"a secret message", buf)
# get the ciphertext from the buffer reading only the bytes written to it (len_encrypted)
ct = bytes(buf[:len_encrypted]) + encryptor.finalize()
decryptor = cipher.decryptor()
len_decrypted = decryptor.update_into(ct, buf)
# get the plaintext from the buffer reading only the bytes written (len_decrypted)
bytes(buf[:len_decrypted]) + decryptor.finalize()