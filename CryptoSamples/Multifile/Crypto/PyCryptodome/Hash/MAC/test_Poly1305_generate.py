from Crypto.Hash import Poly1305
from Crypto.Cipher import AES

secret = b'Thirtytwo very very secret bytes'
mac = Poly1305.new(key=secret, cipher=AES)
mac.update(b'Hello')
print("Nonce: ", mac.nonce.hex())
print("MAC:   ", mac.hexdigest())