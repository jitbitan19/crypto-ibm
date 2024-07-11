from Crypto.Hash import SHA1

h = SHA1.new()
h.update(b'Hello')
print(h.hexdigest())