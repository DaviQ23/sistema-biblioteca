from datetime import date
from functools import reduce
from typing import Iterable

from .models import Emprestimo, Livro


VALOR_MULTA_DIARIA = 2.0


def filtrar_livros_por_categoria(livros: Iterable[Livro], categoria: str) -> list[Livro]:
    return list(filter(lambda livro: livro.categoria.casefold() == categoria.casefold(), livros))


def calcular_multa(dias_atraso: int, valor_diario: float = VALOR_MULTA_DIARIA) -> float:
    return max(0, dias_atraso) * valor_diario


def dias_de_atraso(emprestimo: Emprestimo, data_referencia: date) -> int:
    if not emprestimo.ativo:
        return 0
    return max(0, (data_referencia - emprestimo.data_prevista_devolucao).days)


def emprestimos_ativos_atrasados(
    emprestimos: Iterable[Emprestimo], data_referencia: date
) -> list[Emprestimo]:
    return list(
        filter(
            lambda emprestimo: emprestimo.ativo
            and dias_de_atraso(emprestimo, data_referencia) > 0,
            emprestimos,
        )
    )


def relatorio_multas(
    emprestimos: Iterable[Emprestimo], data_referencia: date
) -> list[dict[str, object]]:
    atrasados = emprestimos_ativos_atrasados(emprestimos, data_referencia)
    return list(
        map(
            lambda emprestimo: {
                "emprestimo_id": emprestimo.identificador,
                "livro_id": emprestimo.livro_id,
                "usuario_id": emprestimo.usuario_id,
                "dias_atraso": dias_de_atraso(emprestimo, data_referencia),
                "multa": calcular_multa(dias_de_atraso(emprestimo, data_referencia)),
            },
            atrasados,
        )
    )


def total_multas(emprestimos: Iterable[Emprestimo], data_referencia: date) -> float:
    valores = map(
        lambda item: float(item["multa"]),
        relatorio_multas(emprestimos, data_referencia),
    )
    return reduce(lambda acumulado, valor: acumulado + valor, valores, 0.0)


def quantidade_livros_por_categoria(livros: Iterable[Livro]) -> dict[str, int]:
    categorias = map(lambda livro: livro.categoria, livros)
    return reduce(
        lambda resultado, categoria: {
            **resultado,
            categoria: resultado.get(categoria, 0) + 1,
        },
        categorias,
        {},
    )


def quantidade_emprestimos_por_usuario(
    emprestimos: Iterable[Emprestimo],
) -> dict[str, int]:
    usuarios = map(lambda emprestimo: emprestimo.usuario_id, emprestimos)
    return reduce(
        lambda resultado, usuario_id: {
            **resultado,
            usuario_id: resultado.get(usuario_id, 0) + 1,
        },
        usuarios,
        {},
    )


def quantidade_emprestimos_ativos(emprestimos: Iterable[Emprestimo]) -> int:
    return len(list(filter(lambda emprestimo: emprestimo.ativo, emprestimos)))


def quantidade_emprestimos_atrasados(
    emprestimos: Iterable[Emprestimo], data_referencia: date
) -> int:
    return len(emprestimos_ativos_atrasados(emprestimos, data_referencia))


def relatorio_imperativo_multas(
    emprestimos: Iterable[Emprestimo], data_referencia: date
) -> float:
    total = 0.0
    for emprestimo in emprestimos:
        if emprestimo.ativo:
            atraso = dias_de_atraso(emprestimo, data_referencia)
            if atraso > 0:
                total += atraso * VALOR_MULTA_DIARIA
    return total
