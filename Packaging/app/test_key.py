from MyCrypto.key import key_gen

password = "secret1234"
key1 = key_gen(
    pwd=password,
    method="PBKDF2",
    hashfn="SHA3_256",
    salt_len=10,
    key_len=32,
)
key2 = key_gen(
    pwd=password,
    method="scrypt",
    hashfn="SHA3_256",
    salt_len=10,
    key_len=32,
)

print(f"Password: {password}")
print(f"PBKDF2 derived key with random salt: {key1}")
print(f"Scrypt derived key with random salt: {key2}")
