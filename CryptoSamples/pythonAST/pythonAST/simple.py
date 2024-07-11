import ast
#strFilePath = "C:/WS-QS/quantum-safe-sca-smoke-test/python/Crypto/PyCrypto/Hash/test_MD5.py"
strFilePath = "AES.py"
with open(strFilePath, "r") as file:
    pyFile = file.read()# replace newline with space 

#ast.parse(pyFile,filename=strFilePath,mode='eval',type_comments=True,feature_version=1)
code = ast.dump(ast.parse(pyFile,filename=strFilePath,mode='exec',type_comments=True),indent=4,annotate_fields=True,include_attributes=True)
print(code)
