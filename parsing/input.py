from Crypto.Hash import SHA3_256, BLAKE2s
import Crypto.Hash.SHA256 as cc

a = 5
b = 2
c = 1
a + b + c
# a = (4 + b) * c

a = (b or c) * a

msg = "Hello"
h1 = SHA3_256.new()
h1 = cc.new()
h1.update(msg.encode())
print(f"SHA3-256   of '{msg}': {h1.hexdigest()}")
