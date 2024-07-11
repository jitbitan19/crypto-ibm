import os
from cryptography.hazmat.primitives.ciphers.aead import AESSIV

data = b"a secret message"
nonce = os.urandom(16)
aad = [b"authenticated but unencrypted data", nonce]
key = AESSIV.generate_key(bit_length=512)  # AES256 requires 512-bit keys for SIV
aessiv = AESSIV(key)
ct = aessiv.encrypt(data, aad)
aessiv.decrypt(ct, aad)