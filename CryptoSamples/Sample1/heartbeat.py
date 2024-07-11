import chromadb
client = chromadb.PersistentClient(path="C:/WS-QS/chromapoc")
print(client.heartbeat()) # returns a nanosecond heartbeat. Useful for making sure the client remains connected.
#collection = client.create_collection(name="my_collection")
collection = client.get_collection(name="my_collection")

#with open("C:/WS-QS/quantum-safe-sca-smoke-test/python/venv/Lib/site-packages/Crypto/Hash/MD5.py", "r") as file:
#    hash = file.read()# replace newline with space
#print(hash)


#collection.add(
#    documents=[hash],
#    metadatas=[{"Hash": "MD5"}],
#    ids=["HashMD5"]
#)
#client.reset()
results = collection.query(
    query_texts=["MD5.new()"],
    n_results=2
)

print(results)