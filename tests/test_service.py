from datetime import date

import pytest

from biblioteca.models import Livro, Usuario
from biblioteca.service import Biblioteca


def criar_biblioteca():
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro(Livro("L1", "Python", "Autora", "Computação"))
    biblioteca.cadastrar_usuario(Usuario("U1", "Ana", "2026001"))
    biblioteca.cadastrar_usuario(Usuario("U2", "Bruno", "2026002"))
    return biblioteca


def test_cadastrar_e_consultar_livro_usuario():
    biblioteca = criar_biblioteca()
    assert biblioteca.consultar_livro("L1").titulo == "Python"
    assert biblioteca.consultar_usuario("U1").nome == "Ana"


def test_impede_identificadores_duplicados():
    biblioteca = criar_biblioteca()
    with pytest.raises(ValueError):
        biblioteca.cadastrar_livro(Livro("L1", "Outro", "Autor", "Categoria"))


def test_impede_matricula_duplicada():
    biblioteca = criar_biblioteca()
    with pytest.raises(ValueError):
        biblioteca.cadastrar_usuario(Usuario("U3", "Carla", "2026001"))


def test_emprestimo_deixa_livro_indisponivel():
    biblioteca = criar_biblioteca()
    biblioteca.registrar_emprestimo("E1", "L1", "U1", date(2026, 2, 1))
    assert biblioteca.livro_disponivel("L1") is False


def test_nao_permite_dois_emprestimos_ativos_do_mesmo_livro():
    biblioteca = criar_biblioteca()
    biblioteca.registrar_emprestimo("E1", "L1", "U1", date(2026, 2, 1))
    with pytest.raises(ValueError):
        biblioteca.registrar_emprestimo("E2", "L1", "U2", date(2026, 2, 2))


def test_devolucao_libera_livro():
    biblioteca = criar_biblioteca()
    biblioteca.registrar_emprestimo("E1", "L1", "U1", date(2026, 2, 1))
    biblioteca.registrar_devolucao("E1", date(2026, 2, 10))
    assert biblioteca.livro_disponivel("L1") is True


def test_nao_permite_devolucao_duplicada():
    biblioteca = criar_biblioteca()
    biblioteca.registrar_emprestimo("E1", "L1", "U1", date(2026, 2, 1))
    biblioteca.registrar_devolucao("E1", date(2026, 2, 10))
    with pytest.raises(ValueError):
        biblioteca.registrar_devolucao("E1", date(2026, 2, 11))
