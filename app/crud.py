from bson import ObjectId
from app.db import get_database
from app.cache import salvar_cache, ler_cache

colecao = get_database()

# CREATE
def cadastrar_aluno(nome, idade, curso):
    novo_aluno = {"nome": nome, "idade": idade, "curso": curso}
    colecao.insert_one(novo_aluno)
    print("✅ Aluno cadastrado com sucesso!")

# READ
def listar_alunos():
    alunos = list(colecao.find())
    salvar_cache("ultimo_lista", [str(a) for a in alunos])
    print("\n📋 Lista de alunos:")
    for aluno in alunos:
        print(aluno)

# UPDATE
def atualizar_aluno(id_aluno, novo_nome):
    colecao.update_one({"_id": ObjectId(id_aluno)}, {"$set": {"nome": novo_nome}})
    print("✏️ Aluno atualizado com sucesso!")

# DELETE
def excluir_aluno(id_aluno):
    colecao.delete_one({"_id": ObjectId(id_aluno)})
    print("🗑️ Aluno excluído com sucesso!")

# CACHE
def mostrar_cache():
    dados = ler_cache("ultimo_lista")
    if dados:
        print("\n📦 Dados armazenados no cache Redis:")
        for d in dados:
            print(d)
    else:
        print("⚠️ Nenhum dado no cache ainda.")
