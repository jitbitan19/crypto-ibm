from MyCrypto.aes import aes_enc, aes_dec
from MyCrypto.key import key_gen

message = "Advanced Encryption Standard"
password = "hello123"
key = key_gen(password, "scrypt", "SHA256", 64, 64, 1 << 10)

cipher = aes_enc(message, key, "blake2s", "GCM")
decipher = aes_dec(cipher, key, "blake2s", "GCM")

print(f"Message: {message}")
print(f"Password: {password}")
print(f"Key derived: {key}")
print(f"Cipher Text: {cipher[0]}")
print(f"IV: {cipher[1]}")
print(f"Plain Text: {decipher[0]}")
