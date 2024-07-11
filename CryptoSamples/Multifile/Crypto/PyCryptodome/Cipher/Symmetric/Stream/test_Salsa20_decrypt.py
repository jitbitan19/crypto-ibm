from Crypto.Cipher import Salsa20

secret = b'*Thirty-two byte (256 bits) key*'
msg_nonce = msg[:8]
ciphertext = msg[8:]
cipher = Salsa20.new(key=secret, nonce=msg_nonce)
plaintext = cipher.decrypt(ciphertext)