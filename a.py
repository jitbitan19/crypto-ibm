# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
# from Crypto.Hash import SHA256

# key_pair = RSA.generate(1024)
# pub_key = key_pair.public_key()
# with open("pub_key_jit.pem", "wb") as f:
#     f.write(pub_key.export_key())

# msg = "Rivest Shamir Adleman"
# signer = PKCS1_v1_5.new(key_pair)
# sign = signer.sign(SHA256.new(msg.encode()))

# with open("output.txt", "wt") as f:
#     f.write(f"Msg: \t{msg}\nSign:\t{sign.hex()}")

print("Hello world")
