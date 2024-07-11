from cryptography.hazmat.primitives.asymmetric import x25519

private_key = x25519.X25519PrivateKey.generate()
public_key = private_key.public_key()
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
loaded_public_key = x25519.X25519PublicKey.from_public_bytes(public_bytes)