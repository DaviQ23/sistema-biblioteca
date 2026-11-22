from datetime import date

from biblioteca.functional import (
    calcular_multa,
    emprestimos_ativos_atrasados,
    filtrar_livros_por_categoria,
    quantidade_emprestimos_ativos,
    quantidade_emprestimos_atrasados,
    quantidade_emprestimos_por_usuario,
    quantidade_livros_por_categoria,
    relatorio_imperativo_multas,
    relatorio_multas,
    total_multas,
)
from biblioteca.models import Emprestimo, Livro


def criar_emprestimos():
    return [
        Emprestimo("E1", "L1", "U1", date(2026, 1, 1), date(2026, 1, 10)),
        Emprestimo("E2", "L2", "U2", date(2026, 1, 2), date(2026, 1, 12)),
        Emprestimo("E3", "L3", "U1", date(2026, 1, 3), date(2026, 1, 5), date(2026, 1, 6)),
    ]


def test_calcular_multa():
    assert calcular_multa(5) == 10.0
    assert calcular_multa(0) == 0.0
    assert calcular_multa(-2) == 0.0


def test_filtrar_livros_sem_alterar_colecao_original():
    livros = [
        Livro("L1", "Livro A", "Autor A", "Computação"),
        Livro("L2", "Livro B", "Autor B", "História"),
    ]
    resultado = filtrar_livros_por_categoria(livros, "computação")
    assert len(resultado) == 1
    assert resultado[0].identificador == "L1"
    assert len(livros) == 2


def test_filtrar_emprestimos_atrasados():
    emprestimos = criar_emprestimos()
    resultado = emprestimos_ativos_atrasados(emprestimos, date(2026, 1, 15))
    assert [item.identificador for item in resultado] == ["E1", "E2"]


def test_relatorio_multas_e_total():
    emprestimos = criar_emprestimos()
    relatorio = relatorio_multas(emprestimos, date(2026, 1, 15))
    assert [item["multa"] for item in relatorio] == [10.0, 6.0]
    assert total_multas(emprestimos, date(2026, 1, 15)) == 16.0


def test_versoes_imperativa_e_funcional_equivalentes():
    emprestimos = criar_emprestimos()
    referencia = date(2026, 1, 15)
    assert total_multas(emprestimos, referencia) == relatorio_imperativo_multas(emprestimos, referencia)


def test_estatisticas():
    livros = [
        Livro("L1", "Livro A", "Autor A", "Computação"),
        Livro("L2", "Livro B", "Autor B", "Computação"),
        Livro("L3", "Livro C", "Autor C", "História"),
    ]
    emprestimos = criar_emprestimos()
    assert quantidade_livros_por_categoria(livros) == {"Computação": 2, "História": 1}
    assert quantidade_emprestimos_por_usuario(emprestimos) == {"U1": 2, "U2": 1}
    assert quantidade_emprestimos_ativos(emprestimos) == 2
    assert quantidade_emprestimos_atrasados(emprestimos, date(2026, 1, 15)) == 2
