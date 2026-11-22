# Guia para o diagrama de classes UML manuscrito

Este guia é uma referência para desenhar o diagrama em papel A4 branco. O desenho final deve ser feito à mão por cada integrante e deve corresponder ao código entregue.

## Classes e atributos

### Livro
- identificador: str
- titulo: str
- autor: str
- categoria: str

### Usuario
- identificador: str
- nome: str
- matricula: str

### Emprestimo
- identificador: str
- livro_id: str
- usuario_id: str
- data_emprestimo: date
- data_prevista_devolucao: date
- data_efetiva_devolucao: Optional[date]
- ativo: bool (propriedade derivada)

### Biblioteca
- _livros: dict[str, Livro]
- _usuarios: dict[str, Usuario]
- _emprestimos: dict[str, Emprestimo]

## Métodos principais

### Biblioteca
- cadastrar_livro(livro)
- cadastrar_usuario(usuario)
- consultar_livro(identificador)
- consultar_usuario(identificador)
- consultar_emprestimo(identificador)
- livro_disponivel(livro_id)
- registrar_emprestimo(identificador, livro_id, usuario_id, data_emprestimo, prazo_dias)
- registrar_devolucao(emprestimo_id, data_devolucao)

### Emprestimo
- ativo

## Relacionamentos e multiplicidades

- Um `Usuario` pode estar associado a zero ou muitos `Emprestimo`.
- Cada `Emprestimo` está associado a exatamente um `Usuario`.
- Um `Livro` pode aparecer em zero ou muitos registros históricos de `Emprestimo`.
- Cada `Emprestimo` está associado a exatamente um `Livro`.
- `Biblioteca` mantém coleções de livros, usuários e empréstimos.

## Sugestão de disposição no papel

Coloque `Biblioteca` no centro ou na parte superior. Abaixo, posicione `Livro`, `Usuario` e `Emprestimo`. Desenhe as associações com multiplicidades e identifique as responsabilidades. Não desenhe métodos que não existam no código.
