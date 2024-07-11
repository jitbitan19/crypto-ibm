from Crypto.Hash import KMAC128

secret = b'Sixteen byte key'
mac = KMAC128.new(key=secret, mac_len=16)
mac.update(b'Hello')
print(mac.hexdigest())