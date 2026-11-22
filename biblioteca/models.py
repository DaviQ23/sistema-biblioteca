from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class Livro:
    identificador: str
    titulo: str
    autor: str
    categoria: str


@dataclass(frozen=True)
class Usuario:
    identificador: str
    nome: str
    matricula: str


@dataclass(frozen=True)
class Emprestimo:
    identificador: str
    livro_id: str
    usuario_id: str
    data_emprestimo: date
    data_prevista_devolucao: date
    data_efetiva_devolucao: Optional[date] = None

    @property
    def ativo(self):
        return self.data_efetiva_devolucao is None
