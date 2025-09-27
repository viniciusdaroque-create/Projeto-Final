# ==============================
# Sistema de Biblioteca Virtual
# ==============================

# Listas principais
livros = []
usuarios = []
emprestimos = []


# ------------------------------
# Funções relacionadas aos Livros
# ------------------------------

def cadastrar_livro():
    nome = input("Digite o título do livro: ").strip()
    livro = {"titulo": nome, "disponivel": True}
    livros.append(livro)
    print(f"Livro '{nome}' cadastrado com sucesso!")


def remover_livro():
    if not livros:
        print("Nenhum livro cadastrado")
        return
    nome = input("Digite o título do livro para removê-lo: ").strip()
    for livro in livros:
        if livro["titulo"].lower() == nome.lower():
            livros.remove(livro)
            print(f"Livro '{nome}' removido com sucesso!")
            return
    print(f"Livro '{nome}' não encontrado")


def exibir_livros():
    if not livros:
        print("Nenhum livro cadastrado")
    else:
        for i, livro in enumerate(livros, start=1):
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"{i} - {livro['titulo']} ({status})")


# ------------------------------
# Funções relacionadas aos Usuários
# ------------------------------

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    usuario = {"nome": nome, "idade": idade}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def exibir_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']} | Idade: {usuario['idade']}")


# ------------------------------
# Funções relacionadas a Empréstimos
# ------------------------------

def emprestar_livro():
    if not usuarios:
        print("Nenhum usuário cadastrado")
        return
    if not livros:
        print("Nenhum livro cadastrado")
        return

    exibir_usuarios()
    usuario_idx = int(input("Digite o número do usuário: ")) - 1
    if usuario_idx < 0 or usuario_idx >= len(usuarios):
        print("Usuário inválido")
        return

    exibir_livros()
    livro_idx = int(input("Digite o número do livro para emprestar: ")) - 1
    if livro_idx < 0 or livro_idx >= len(livros):
        print("Livro inválido!")
        return

    if not livros[livro_idx]["disponivel"]:
        print("Esse livro já está emprestado.")
        return

    # Registrar empréstimo
    livros[livro_idx]["disponivel"] = False
    emprestimo = {
        "usuario": usuarios[usuario_idx]["nome"],
        "livro": livros[livro_idx]["titulo"]
    }
    emprestimos.append(emprestimo)
    print(f"O livro '{livros[livro_idx]['titulo']}' foi emprestado para {usuarios[usuario_idx]['nome']}.")


def listar_emprestimos():
    if not emprestimos:
        print("Nenhum empréstimo registrado.")
    else:
        print("Empréstimos ativos:")
        for i, emp in enumerate(emprestimos, start=1):
            print(f"{i}. Usuário: {emp['usuario']} | Livro: {emp['livro']}")


# ------------------------------
# Menu principal
# ------------------------------

while True:
    print("\n=== Biblioteca Virtual ===")
    print("1 - Cadastrar Livro")
    print("2 - Remover Livro")
    print("3 - Exibir Lista de Livros")
    print("4 - Cadastrar Usuário")
    print("5 - Exibir Lista de Usuários")
    print("6 - Emprestar Livro")
    print("7 - Listar Empréstimos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        remover_livro()
    elif opcao == "3":
        exibir_livros()
    elif opcao == "4":
        cadastrar_usuario()
    elif opcao == "5":
        exibir_usuarios()
    elif opcao == "6":
        emprestar_livro()
    elif opcao == "7":
        listar_emprestimos()
    elif opcao == "0":
        print("Encerrando o sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")



   
