from Crypto.Cipher import Salsa20

plaintext = b'Attack at dawn'
secret = b'*Thirty-two byte (256 bits) key*'
cipher = Salsa20.new(key=secret)
msg = cipher.nonce + cipher.encrypt(plaintext)