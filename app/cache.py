import redis
import json

# Conexão simples com Redis
cache = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def salvar_cache(chave, valor):
    cache.set(chave, json.dumps(valor))

def ler_cache(chave):
    valor = cache.get(chave)
    return json.loads(valor) if valor else None
