# Sistema de Gerenciamento de Biblioteca

Projeto acadêmico da disciplina Paradigmas de Linguagens de Programação. O sistema demonstra integração entre Programação Orientada a Objetos (POO) e Programação Funcional (PF), conforme o enunciado da atividade.

## Funcionalidades

- Cadastro e consulta de livros e usuários
- Registro de empréstimos e devoluções
- Controle de disponibilidade de cada exemplar
- Identificação de empréstimos ativos em atraso
- Cálculo de multa de R$ 2,00 por dia de atraso
- Relatório individual e total de multas
- Estatísticas de livros, usuários e empréstimos
- Filtro de livros por categoria
- Comparação entre implementação imperativa e funcional

## Tecnologias

- Python 3.10 ou superior
- pytest para testes automatizados

Não é necessário banco de dados. Os dados ficam em memória durante a execução.

## Estrutura do projeto

```text
sistema_biblioteca/
├── app.py
├── biblioteca/
│   ├── __init__.py
│   ├── functional.py
│   ├── models.py
│   └── service.py
├── tests/
│   ├── test_functional.py
│   └── test_service.py
├── docs/
│   ├── guia_diagrama_classes.md
│   ├── guia_fluxo_funcional.md
│   └── roteiro_questoes_individuais.md
├── requirements.txt
└── README.md
```

## Como executar

1. Instale Python 3.10 ou superior.
2. Crie e ative um ambiente virtual:

   Windows:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   Linux/macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o sistema:

   ```bash
   python app.py
   ```

## Como executar os testes

Na raiz do projeto:

```bash
python -m pytest -v
```

## Modelagem orientada a objetos

O sistema contém as quatro classes exigidas:

- `Livro`: representa um exemplar do acervo.
- `Usuario`: representa uma pessoa cadastrada.
- `Emprestimo`: representa a relação de empréstimo entre um usuário e um livro, com datas.
- `Biblioteca`: coordena cadastros, consultas, empréstimos e devoluções.

`Livro`, `Usuario` e `Emprestimo` são dataclasses imutáveis (`frozen=True`). Na devolução, o empréstimo anterior não é alterado: uma nova instância com a data efetiva é criada e armazenada pela biblioteca.

## Programação funcional

O módulo `biblioteca/functional.py` concentra funções de consulta e cálculo que não alteram as coleções recebidas.

- `filter`: filtro de livros por categoria e seleção de empréstimos atrasados.
- `map`: transformação de empréstimos atrasados em itens de relatório.
- `reduce`: soma das multas e agregação de estatísticas.
- Funções puras: `calcular_multa`, `dias_de_atraso`, `relatorio_multas`, `total_multas` e funções de estatística.

A data de referência é recebida como parâmetro para que os cálculos sejam reproduzíveis e testáveis.

## Regras de negócio adotadas

- Cada livro cadastrado representa um exemplar único.
- Um usuário pode ter vários empréstimos.
- Cada empréstimo está associado a um único livro e a um único usuário.
- Um livro com empréstimo ativo não pode ser emprestado novamente.
- O prazo padrão de empréstimo é de 14 dias, contado a partir da data do empréstimo.
- A devolução registra a data efetiva e torna o livro disponível.
- Um empréstimo ativo é considerado atrasado quando a data de referência é posterior à data prevista de devolução.
- A multa é de R$ 2,00 por dia de atraso.
- O relatório de multas considera somente empréstimos ativos e atrasados.
- Reservas e múltiplas cópias não são implementadas.

## Exemplo de cálculo

Se a data prevista de devolução for 10/03/2026 e a data de referência for 15/03/2026, existem cinco dias de atraso. A multa será:

`5 × R$ 2,00 = R$ 10,00`

## Programação imperativa e funcional

O módulo `biblioteca/functional.py` contém duas versões do cálculo total de multas:

- `total_multas`: versão funcional, utilizando `map` e `reduce` após a filtragem.
- `relatorio_imperativo_multas`: versão imperativa, utilizando laços e acumulador.

As duas devem produzir o mesmo resultado para as mesmas entradas.

## Imutabilidade e efeitos colaterais

As entidades são imutáveis e as funções funcionais não modificam coleções recebidas. A classe `Biblioteca` mantém o estado em memória e realiza operações de cadastro, empréstimo e devolução. Essa separação permite distinguir cálculos puros das operações que produzem efeitos colaterais.

## Observação sobre concorrência

A implementação impede dois empréstimos ativos do mesmo livro em uma execução sequencial. Como não utiliza banco de dados nem mecanismo de sincronização, não oferece garantia contra duas requisições simultâneas em um ambiente concorrente. Funções puras e imutabilidade, isoladamente, não resolvem essa condição de corrida.


## Integrantes

Camila Catalano de Vasconcelos
Gabriela Soares da Silva
