from datetime import date, datetime

from biblioteca.functional import (
    filtrar_livros_por_categoria,
    quantidade_emprestimos_ativos,
    quantidade_emprestimos_atrasados,
    quantidade_emprestimos_por_usuario,
    quantidade_livros_por_categoria,
    relatorio_multas,
    total_multas,
)
from biblioteca.models import Livro, Usuario
from biblioteca.service import Biblioteca


def ler_data(mensagem: str) -> date:
    while True:
        valor = input(mensagem).strip()
        try:
            return datetime.strptime(valor, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Utilize DD/MM/AAAA.")


def mostrar_menu() -> None:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Listar livros")
    print("4. Filtrar livros por categoria")
    print("5. Registrar empréstimo")
    print("6. Registrar devolução")
    print("7. Listar empréstimos")
    print("8. Relatório de multas")
    print("9. Estatísticas")
    print("0. Sair")


def executar() -> None:
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                id = input("ID: ").strip();
                titulo = input("Título: ").strip();
                autor = input("Autor: ").strip();
                categoria = input("Categoria: ").strip();

                livro = Livro(
                    id,
                    titulo,
                    autor,
                    categoria,
                )

                biblioteca.cadastrar_livro(livro)
                print("Livro cadastrado.")

            elif opcao == "2":
                id = input("ID: ").strip();
                nome = input("Nome: ").strip();
                matricula = input("Matrícula: ").strip();

                usuario = Usuario(
                    id,
                    nome,
                    matricula
                )

                biblioteca.cadastrar_usuario(usuario)
                print("Usuário cadastrado.")

            elif opcao == "3":
                for livro in biblioteca.livros:
                    print(f"{livro.identificador} | {livro.titulo} | {livro.autor} | {livro.categoria} | Disponível: {biblioteca.livro_disponivel(livro.identificador)}")

            elif opcao == "4":
                categoria = input("Categoria: ").strip()
                encontrados = filtrar_livros_por_categoria(biblioteca.livros, categoria)
                for livro in encontrados:
                    print(f"{livro.identificador} | {livro.titulo} | {livro.autor}")

            elif opcao == "5":
                idEmprestimo = input("ID do empréstimo: ").strip();
                idLivro = input("ID do livro: ").strip();
                idUsuario = input("ID do usuário: ").strip();
                dataEmprestimo = ler_data("Data do empréstimo (DD/MM/AAAA): ");

                emprestimo = biblioteca.registrar_emprestimo(
                    idEmprestimo,
                    idLivro,
                    idUsuario,
                    dataEmprestimo
                )
                print(f"Empréstimo registrado. Devolução prevista: {emprestimo.data_prevista_devolucao:%d/%m/%Y}")

            elif opcao == "6":
                idEmprestimo = input("ID do empréstimo: ").strip();
                dataDevolucao = ler_data("Data da devolução (DD/MM/AAAA): ");

                emprestimo = biblioteca.registrar_devolucao(
                    idEmprestimo,
                    dataDevolucao
                )
                print(f"Devolução registrada para {emprestimo.livro_id}.")

            elif opcao == "7":
                for emprestimo in biblioteca.emprestimos:
                    print(f"{emprestimo.identificador} | Livro: {emprestimo.livro_id} | Usuário: {emprestimo.usuario_id} | Prevista: {emprestimo.data_prevista_devolucao:%d/%m/%Y} | Devolvido: {emprestimo.data_efetiva_devolucao:%d/%m/%Y}")

            elif opcao == "8":
                referencia = ler_data("Data de referência (DD/MM/AAAA): ")
                for item in relatorio_multas(biblioteca.emprestimos, referencia):
                    print(item)
                print(f"Total de multas: R$ {total_multas(biblioteca.emprestimos, referencia):.2f}")

            elif opcao == "9":
                referencia = ler_data("Data de referência (DD/MM/AAAA): ")
                print("Livros por categoria:", quantidade_livros_por_categoria(biblioteca.livros))
                print("Empréstimos por usuário:", quantidade_emprestimos_por_usuario(biblioteca.emprestimos))
                print("Empréstimos ativos:", quantidade_emprestimos_ativos(biblioteca.emprestimos))
                print("Empréstimos atrasados:", quantidade_emprestimos_atrasados(biblioteca.emprestimos, referencia))
                print("Total de multas: R$", f"{total_multas(biblioteca.emprestimos, referencia):.2f}")

            elif opcao == "0":
                print("Até logo!")
                break

            else:
                print("Opção inválida.")

        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    executar()
