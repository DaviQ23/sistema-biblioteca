# Roteiro de estudo das cinco questões individuais

As respostas finais devem ser redigidas à mão por cada integrante, com suas próprias palavras. Use este roteiro para estudar e conferir se a explicação está de acordo com o código.

## A) Escolha uma função pura implementada e explique por que possui transparência referencial.

Ponto de partida: `calcular_multa(dias_atraso, valor_diario)`. Para os mesmos argumentos, retorna sempre o mesmo resultado. Não consulta nem modifica estado externo e não realiza entrada ou saída. Por isso, a chamada pode ser substituída pelo valor retornado sem alterar o comportamento do programa.

## B) Identifique uma operação impura e explique por que não é uma função pura.

Ponto de partida: `Biblioteca.registrar_emprestimo`. Ela altera o dicionário interno de empréstimos da biblioteca. Seu efeito pode ser observado posteriormente, pois muda o estado do sistema. A leitura e escrita no terminal em `app.py` também são efeitos externos.

## C) Explique como a imutabilidade foi aplicada e quais problemas ajuda a evitar.

Ponto de partida: as classes `Livro`, `Usuario` e `Emprestimo` usam `@dataclass(frozen=True)`. Não é possível alterar seus atributos após a criação. Na devolução, uma nova instância de `Emprestimo` é criada com a data efetiva, em vez de modificar a instância anterior. As funções de processamento retornam novas listas ou estruturas e não alteram as coleções recebidas. Isso reduz alterações acidentais, facilita testes e torna o fluxo de dados mais previsível.

## D) Compare as versões imperativa e funcional quanto a legibilidade, manutenção, mutabilidade e efeitos colaterais.

Ponto de partida: compare `relatorio_imperativo_multas` e `total_multas`. A versão imperativa percorre os empréstimos, usa condicionais e atualiza um acumulador. A versão funcional compõe filtragem, transformação e agregação com `filter`, `map` e `reduce`. Ambas calculam o mesmo total. A versão funcional evita modificar os dados de entrada; a imperativa usa uma variável local acumuladora, mas também não altera os empréstimos.

## E) Se dois usuários tentarem emprestar simultaneamente o mesmo livro, qual problema pode ocorrer? Funções puras e imutabilidade bastam para evitá-lo? Justifique.

Ponto de partida: pode ocorrer uma condição de corrida. Duas operações podem verificar que o livro está disponível antes de qualquer uma registrar o empréstimo, permitindo dois empréstimos ativos. Funções puras e imutabilidade não garantem exclusão mútua nem atomicidade. Seria necessário controlar a concorrência, por exemplo com bloqueio ou transação em um armazenamento compartilhado. A implementação deste projeto é sequencial e não oferece essa garantia em execução concorrente.

## Preparação para a apresentação

Cada integrante deve conseguir explicar:
- Por que as entidades são imutáveis.
- Como a disponibilidade é calculada.
- Como a devolução libera o livro.
- Como são calculados os dias de atraso.
- Onde estão `map`, `filter` e `reduce`.
- Qual é a diferença entre função pura e operação com efeito colateral.
- Por que a implementação não garante segurança em concorrência.
