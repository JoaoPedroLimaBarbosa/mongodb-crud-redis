from pymongo import MongoClient

# Configuração da conexão
MONGO_URI = "mongodb+srv://joaopedrolimabarbosa007_db_user:jp15@cluster0.es2xd3a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DB = "bd_trabalho"
MONGO_COLLECTION = "alunos"

# Função para conectar
def get_database():
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    return db[MONGO_COLLECTION]
