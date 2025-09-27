import pytest
from projeto_final import livros, usuarios, emprestimos, cadastrar_livro, remover_livro, emprestar_livro


@pytest.fixture(autouse=True)
def setup():
    livros.clear()
    usuarios.clear()
    emprestimos.clear()


# ---- TESTES ----
def test_cadastrar_livro():
    cadastrar_livro_manual("Dom Casmurro")  
    assert len(livros) == 1
    assert livros[0]["titulo"] == "Dom Casmurro"
    assert livros[0]["disponivel"] is True


def test_remover_livro():
    cadastrar_livro_manual("Dom Casmurro")
    remover_livro_manual("Dom Casmurro")
    assert len(livros) == 0


def test_emprestar_livro():
    usuarios.append({"nome": "Maria", "idade": "25"})
    cadastrar_livro_manual("Dom Casmurro")

    emprestar_livro_manual("Maria", "Dom Casmurro")

    assert livros[0]["disponivel"] is False
    assert emprestimos[0]["usuario"] == "Maria"
    assert emprestimos[0]["livro"] == "Dom Casmurro"



def cadastrar_livro_manual(nome):
    livro = {"titulo": nome, "disponivel": True}
    livros.append(livro)


def remover_livro_manual(nome):
    for livro in livros:
        if livro["titulo"].lower() == nome.lower():
            livros.remove(livro)
            break


def emprestar_livro_manual(usuario_nome, livro_nome):
    for livro in livros:
        if livro["titulo"].lower() == livro_nome.lower() and livro["disponivel"]:
            livro["disponivel"] = False
            emprestimos.append({"usuario": usuario_nome, "livro": livro_nome})
            break
