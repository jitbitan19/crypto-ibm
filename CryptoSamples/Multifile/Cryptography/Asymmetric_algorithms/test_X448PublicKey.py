from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x448

private_key = x448.X448PrivateKey.generate()
public_key = private_key.public_key()
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
loaded_public_key = x448.X448PublicKey.from_public_bytes(public_bytes)