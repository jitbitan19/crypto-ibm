import os
from cryptography.hazmat.primitives.ciphers.aead import AESOCB3

data = b"a secret message"
aad = b"authenticated but unencrypted data"
key = AESOCB3.generate_key(bit_length=128)
aesocb = AESOCB3(key)
nonce = os.urandom(12)
ct = aesocb.encrypt(nonce, data, aad)
aesocb.decrypt(nonce, ct, aad)