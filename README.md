##**Universidade Federal de Sergipe**##

● **Corretor Ortográfico**

Este projeto foi desenvolvido como parte das atividades acadêmicas avaliativas da disciplina de Matemática Discreta, ministrada pelo professor Gastão Florêncio Miranda Junior. O objetivo desta atividade é implementar um corretor ortográfico utilizando três diferentes medidas de distância entre palavras. O projeto será avaliado com base na correta implementação dos algoritmos e na análise crítica dos resultados obtidos. O banco de palavras utilizado está contido no arquivo br-sem-acentos.txt, o qual contém palavras com letras maiúsculas e sem acentuação.

● **Funcionalidades**
1. Cálculo de Distâncias
Foram desenvolvidos três algoritmos para calcular a distância entre duas palavras, conforme descrito a seguir:

▸ **Distância de edição (Levenshtein)**: Mede o número mínimo de operações necessárias para transformar uma palavra em outra.

▸ **Distância euclidiana**: Calcula a distância geométrica entre as representações numéricas das palavras, considerando a ordenação das letras segundo a tabela ASCII.

▸ **Distância angular**: Baseia-se na diferença angular entre as representações vetoriais das palavras, também utilizando a ordenação ASCII.

2. Corretor Ortográfico

Implementamos um corretor ortográfico que utiliza as três distâncias mencionadas (Levenshtein, Euclidiana e Angular) para sugerir palavras corretas com base em uma palavra incorreta fornecida. A linguagem de programação utilizada para a implementação pode ser escolhida de acordo com a preferência do desenvolvedor.

3. Comparação de Sugestões

Com o intuito de avaliar o desempenho de cada métrica, foram realizadas comparações entre as sugestões geradas para um conjunto de 10 palavras com erros ortográficos. Para cada palavra, foi gerada uma tabela contendo até 5 sugestões de correção, juntamente com as respectivas distâncias calculadas.

● **Resultados**
Os resultados incluem uma análise detalhada da eficiência de cada uma das três distâncias na tarefa de correção ortográfica. O desempenho foi avaliado em termos da qualidade das sugestões oferecidas, assim como da precisão de cada abordagem.

**EM DESENVOLVIMENTO !!!**
