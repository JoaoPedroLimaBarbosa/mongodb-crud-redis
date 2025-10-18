# CRUD com MongoDB Atlas e Redis

## 💡 Descrição
Aplicação simples em Python que realiza operações CRUD em uma coleção de alunos no MongoDB Atlas, com cache no Redis.

## 🚀 Tecnologias
- Python
- PyMongo
- Redis

## ⚙️ Funcionalidades
- Cadastrar alunos
- Listar alunos
- Atualizar alunos
- Excluir alunos
- Armazenar dados temporários no Redis

## 🧩 Estrutura do Projeto
app/
├── db.py
├── cache.py
└── crud.py
main.py
requirements.txt
README.md


## ▶️ Execução
1. Inicie o Redis localmente (`redis-server`).
2. No terminal do VS Code, execute:
   ```bash
   python main.py


---

## 🧠 ETAPA 8 — Testar tudo

1. Abra `main.py` no VS Code.  
2. Clique com o botão direito → **Run Python File**.  
3. Teste cadastrar, listar, atualizar e excluir alunos.  
4. Depois veja se o cache aparece com a opção “Mostrar cache (Redis)”.

---

