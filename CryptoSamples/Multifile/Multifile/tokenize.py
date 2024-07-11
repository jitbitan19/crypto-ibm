import tokenize
from io import BytesIO

def tokenize_code(code):
    tokens = []
    reader = BytesIO(code.encode('utf-8')).readline
    for token in tokenize.tokenize(reader):
        tokens.append(token)
    return tokens

with open("C:/WS-QS/quantum-safe-sca-smoke-test/python/Multifile/crypto_module/utils.py", "r") as file:
  code = file.read()
  print(code)  
tokens = tokenize_code(code)
for token in tokens:
    print(token)