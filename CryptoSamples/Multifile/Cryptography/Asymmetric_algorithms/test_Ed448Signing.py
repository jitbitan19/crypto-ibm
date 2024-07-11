from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey

private_key = Ed448PrivateKey.generate()
signature = private_key.sign(b"my authenticated message")
public_key = private_key.public_key()
# Raises InvalidSignature if verification fails
public_key.verify(signature, b"my authenticated message")