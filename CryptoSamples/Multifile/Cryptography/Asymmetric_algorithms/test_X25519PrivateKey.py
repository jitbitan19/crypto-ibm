from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519

private_key = x25519.X25519PrivateKey.generate()
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
)
loaded_private_key = x25519.X25519PrivateKey.from_private_bytes(private_bytes)