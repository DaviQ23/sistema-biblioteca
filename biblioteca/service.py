from datetime import date, timedelta

from .models import Emprestimo, Livro, Usuario


class Biblioteca:
    def __init__(self):
        self._livros: dict[str, Livro] = {}
        self._usuarios: dict[str, Usuario] = {}
        self._emprestimos: dict[str, Emprestimo] = {}

    @property
    def livros(self) -> tuple[Livro, ...]:
        return tuple(self._livros.values())

    @property
    def usuarios(self) -> tuple[Usuario, ...]:
        return tuple(self._usuarios.values())

    @property
    def emprestimos(self) -> tuple[Emprestimo, ...]:
        return tuple(self._emprestimos.values())

    def cadastrar_livro(self, livro: Livro) -> None:
        if livro.identificador in self._livros:
            raise ValueError("Já existe um livro com esse identificador.")
        self._livros[livro.identificador] = livro

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        if usuario.identificador in self._usuarios:
            raise ValueError("Já existe um usuário com esse identificador.")
        if any(item.matricula == usuario.matricula for item in self._usuarios.values()):
            raise ValueError("Já existe um usuário com essa matrícula.")
        self._usuarios[usuario.identificador] = usuario

    def consultar_livro(self, identificador: str) -> Livro:
        try:
            return self._livros[identificador]
        except KeyError as exc:
            raise ValueError("Livro não encontrado.") from exc

    def consultar_usuario(self, identificador: str) -> Usuario:
        try:
            return self._usuarios[identificador]
        except KeyError as exc:
            raise ValueError("Usuário não encontrado.") from exc

    def consultar_emprestimo(self, identificador: str) -> Emprestimo:
        try:
            return self._emprestimos[identificador]
        except KeyError as exc:
            raise ValueError("Empréstimo não encontrado.") from exc

    def livro_disponivel(self, livro_id: str) -> bool:
        self.consultar_livro(livro_id)
        return not any(
            emprestimo.livro_id == livro_id and emprestimo.ativo
            for emprestimo in self._emprestimos.values()
        )

    def registrar_emprestimo(
        self,
        identificador: str,
        livro_id: str,
        usuario_id: str,
        data_emprestimo: date,
        prazo_dias: int = 14,
    ) -> Emprestimo:
        if identificador in self._emprestimos:
            raise ValueError("Já existe um empréstimo com esse identificador.")
        if prazo_dias <= 0:
            raise ValueError("O prazo deve ser maior que zero.")
        self.consultar_livro(livro_id)
        self.consultar_usuario(usuario_id)
        if not self.livro_disponivel(livro_id):
            raise ValueError("Livro indisponível para empréstimo.")
        emprestimo = Emprestimo(
            identificador=identificador,
            livro_id=livro_id,
            usuario_id=usuario_id,
            data_emprestimo=data_emprestimo,
            data_prevista_devolucao=data_emprestimo + timedelta(days=prazo_dias),
        )
        self._emprestimos[identificador] = emprestimo
        return emprestimo

    def registrar_devolucao(self, emprestimo_id: str, data_devolucao: date) -> Emprestimo:
        emprestimo = self.consultar_emprestimo(emprestimo_id)
        if not emprestimo.ativo:
            raise ValueError("Esse empréstimo já foi devolvido.")
        if data_devolucao < emprestimo.data_emprestimo:
            raise ValueError("A devolução não pode ocorrer antes do empréstimo.")
        atualizado = Emprestimo(
            identificador=emprestimo.identificador,
            livro_id=emprestimo.livro_id,
            usuario_id=emprestimo.usuario_id,
            data_emprestimo=emprestimo.data_emprestimo,
            data_prevista_devolucao=emprestimo.data_prevista_devolucao,
            data_efetiva_devolucao=data_devolucao,
        )
        self._emprestimos[emprestimo_id] = atualizado
        return atualizado
