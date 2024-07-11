import chromadb
from chromadb.utils import embedding_functions

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chromapoc")
print(client.heartbeat()) # returns a nanosecond heartbeat. Useful for making sure the client remains connected.
collection = client.get_or_create_collection(name="my_collection",embedding_function=sentence_transformer_ef)
#collection = client.get_collection(name="my_collection")
documents=[]
metadatas=[]
ids=[]
id=1
with open("C:/WS-QS/quantum-safe-sca-smoke-test/python/venv/Lib/site-packages/Crypto/Hash/MD5.py", "r") as file:
    for line in file:
         documents.append(line.strip())
         metadatas.append({"item_id": id})
         ids.append(str(id))
         id+=1
collection.add(
   documents=documents,
   metadatas=metadatas,
   ids=ids
)

results = collection.query(
    query_texts=["MD5.new()"],
    n_results=2
)
print(results)