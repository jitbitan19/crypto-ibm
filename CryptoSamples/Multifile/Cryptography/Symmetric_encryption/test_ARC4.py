from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message")
decryptor = cipher.decryptor()
decryptor.update(ct)