from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x448

private_key = x448.X448PrivateKey.generate()
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
)
loaded_private_key = x448.X448PrivateKey.from_private_bytes(private_bytes)