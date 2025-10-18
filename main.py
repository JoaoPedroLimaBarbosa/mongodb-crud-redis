from app.crud import cadastrar_aluno, listar_alunos, atualizar_aluno, excluir_aluno, mostrar_cache

def menu():
    while True:
        print("\n=== SISTEMA CRUD COM MONGODB E REDIS ===")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Excluir aluno")
        print("5. Mostrar cache (Redis)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            cadastrar_aluno(nome, idade, curso)
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            id_aluno = input("ID do aluno para atualizar: ")
            novo_nome = input("Novo nome: ")
            atualizar_aluno(id_aluno, novo_nome)
        elif opcao == "4":
            id_aluno = input("ID do aluno para excluir: ")
            excluir_aluno(id_aluno)
        elif opcao == "5":
            mostrar_cache()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    menu()
