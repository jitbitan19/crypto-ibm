from Crypto.Hash import KMAC256

secret = b'Protect this thirty-two byte key'
mac = KMAC256.new(key=secret, mac_len=16)
mac.update(b'Hello')
print(mac.hexdigest())