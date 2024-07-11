from MyCrypto.rsa import gen_rsa_key, rsa_enc, rsa_dec

nn = "jb"
gen_rsa_key(1024, nn)

message = "Rivest-Shamir-Adleman"
ct = rsa_enc(msg=message, key_name=nn)
pt = rsa_dec(cipher=ct, key_name=nn)

print(f"Message: {message}")
print(f"Cipher Text: {ct}")
print(f"Plain Text: {pt}")
