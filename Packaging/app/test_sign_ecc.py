from MyCrypto.sign_ecc import gen_ecc_sign_key, ecc_sign, ecc_verify

# nn = "jb"
# gen_ecc_sign_key(nn, "p256")
# message = "Package used Pycryptodome"
# sign = ecc_sign(message, nn)
# val = ecc_verify(message, sign, nn)

nn = "jb"
gen_ecc_sign_key(nn, "p256")
message = "Package used Pycryptodome"
sign = ecc_sign(message, nn)
val = ecc_verify(message, sign, nn)

print(f"Message: {message}")
print(f"Signature: {sign}")
print(f"Sign Validity: {val}")
