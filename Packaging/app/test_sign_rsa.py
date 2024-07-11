from MyCrypto.sign_rsa import gen_rsa_sign_key, rsa_sign, rsa_verify

nn = "jb"
gen_rsa_sign_key(1024, nn)
message = "Package used Pycryptodome"
sign = rsa_sign(message, nn)
val = rsa_verify(message, sign, nn)

print(f"Message: {message}")
print(f"Signature: {sign}")
print(f"Sign Validity: {val}")
