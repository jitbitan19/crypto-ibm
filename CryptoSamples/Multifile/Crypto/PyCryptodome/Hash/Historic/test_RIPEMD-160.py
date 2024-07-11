from Crypto.Hash import RIPEMD160

h = RIPEMD160.new()
h.update(b'Hello')
print(h.hexdigest())