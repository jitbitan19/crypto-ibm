from cryptography.hazmat.primitives import padding

padder = padding.ANSIX923(128).padder()
padded_data = padder.update(b"11111111111111112222222222")
print(padded_data)
padded_data += padder.finalize()
print(padded_data)
unpadder = padding.ANSIX923(128).unpadder()
data = unpadder.update(padded_data)
print(data)
print(data + unpadder.finalize())