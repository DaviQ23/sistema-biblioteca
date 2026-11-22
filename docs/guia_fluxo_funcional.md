# Guia para o diagrama de fluxo funcional manuscrito

O diagrama deve representar o caminho real do relatório de multas no código.

## Fluxo sugerido

1. `Biblioteca.emprestimos`
   - Entrada: coleção de empréstimos armazenados.
   - Saída: tupla de empréstimos.
   - Tipo: acesso ao estado da biblioteca; operação de consulta.

2. `emprestimos_ativos_atrasados(emprestimos, data_referencia)`
   - Entrada: coleção e data de referência.
   - Operação: `filter`.
   - Saída: lista de empréstimos ativos com atraso.
   - Tipo: função pura.

3. `dias_de_atraso(emprestimo, data_referencia)`
   - Entrada: empréstimo e data de referência.
   - Saída: quantidade de dias de atraso.
   - Tipo: função pura.

4. `calcular_multa(dias_atraso, 2.0)`
   - Entrada: dias de atraso e valor diário.
   - Saída: valor da multa.
   - Tipo: função pura.

5. `relatorio_multas(emprestimos, data_referencia)`
   - Operação: `map`.
   - Entrada: empréstimos atrasados.
   - Saída: lista de registros com identificadores, dias de atraso e multa.
   - Tipo: função pura.

6. `total_multas(emprestimos, data_referencia)`
   - Operações: `map` para obter os valores e `reduce` para somar.
   - Entrada: coleção de empréstimos e data de referência.
   - Saída: valor total das multas.
   - Tipo: função pura.

7. Exibição no terminal (`app.py`)
   - Entrada: relatório e total calculado.
   - Saída: informações apresentadas ao usuário.
   - Tipo: operação impura, pois realiza saída no terminal.

## Como desenhar

Use um bloco por etapa e conecte-os com setas. Em cada bloco, escreva o nome da função, dados recebidos, resultado produzido, classificação pura/impura e operação funcional utilizada, quando aplicável.

Importante: `total_multas` chama `relatorio_multas`, que por sua vez filtra e mapeia os empréstimos. O cálculo total aplica outro `map` e um `reduce` para somar os valores.
