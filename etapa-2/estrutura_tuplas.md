# Fundamentos de Python (Tipos Compostos) parte 2

## Tuplas

Outro tipo de objeto básico do Python é a *tupla* (uma coleção de outros objetos que não pode ser alterada - imutável). Conforme você verá a tupla é um objeto relativamente simples que, de modo geral, executa operações sobre as quais você já aprendeu quando estudou as strings e as listas.

As tuplas constróem grupos de objetos simples. Elas funcionam exatamente como as listas, exceto que não podem ser alteradas no local (são imutáveis) e, normalmente, são escritas como uma série de itens entre parênteses e não entre colchetes. Embora possuam poucos métodos próprios (`count` e `index`), as tuplas compartilham muitas operações com listas. As tuplas:

* *São coleções ordenadas de objetos arbitrários*

* *São acessadas pelo deslocamento*

* *São de categoria seqüêncial imutável*

* *Tem comprimento fixo, são heterogêneas e podem ser aninhadas arbitrariamente*

* *São arrays de referência de objeto*

## Operações comuns com Tuplas no Python

*Tabela 1.3*

| Operação                      | Exemplo            | Descrição                                                         |
| ----------------------------- | ------------------ | ----------------------------------------------------------------- |
| Criar uma tupla               | `t = (1, 2, 3)`    | Declaração simples de uma tupla.                                  |
| Indexação                     | `t[0]`             | Acessa o elemento pelo índice.                                    |
| Fatiamento (slice)            | `t[1:]`            | Retorna uma nova tupla com parte dos elementos.                   |
| Concatenação                  | `(1, 2) + (3, 4)`  | Junta duas tuplas.                                                |
| Repetição                     | `(1, 2) * 2`       | Repete os elementos da tupla.                                     |
| Verificar elemento            | `3 in t`           | Checa se um elemento está presente.                               |
| Comprimento                   | `len(t)`           | Retorna a quantidade de elementos.                                |
| Contar ocorrências            | `t.count(2)`       | Conta quantas vezes um elemento aparece.                          |
| Encontrar índice              | `t.index(3)`       | Retorna o índice da primeira ocorrência do elemento.              |
| Desempacotamento              | `a, b, c = t`      | Atribui os valores da tupla a variáveis.                          |
| Tupla de 1 elemento           | `t = (1,)`         | É necessário a vírgula para criar uma tupla de um único elemento. |
| Converter para lista          | `list(t)`          | Converte a tupla em uma lista mutável.                            |
| Converter de lista para tupla | `tuple([1, 2, 3])` | Converte uma lista em tupla imutável.                             |

As tuplas são escritas como uma série de objetos (na realidade, expressões que geram objetos), separados por vírgula e incluídos entre parênteses. Uma tupla vazia é apenas um par de parênteses sem nada dentro.

```python
>>> (1, 2) + (3, 4)  # Concatenação de uma tupla.
(1, 2, 3, 4)
>>> (1, 2) * 4  # Repetição dos elementos.
(1, 2, 1, 2, 1, 2, 1, 2)
>>> T = (1, 2, 3, 4)  # Cria uma tupla e adiciona a uma variável.
>>> T
(1, 2, 3, 4)
>>> T[0], T[1:3]  # Indexação e fracionamento (slice) de uma tupla.
(1, (2, 3))
>>> T = ()  # Cria uma tupla vazia.
>>> T
()
>>> x = (42,)  # Tupla de um único elemento (necessário usar vírgula).
>>> x
(42,)
>>> len((1, 2, 3))  # Comprimento da tupla.
3
>>> 3 in (1, 2, 3)  # Verifica se um elemento está presente.
True
>>> (1, 2, 3).count(2)  # Conta quantas vezes o elemento aparece.
1
>>> (1, 2, 3).index(3)  # Retorna o índice do elemento.
2
>>> a, b, c = (1, 2, 3)  # Desempacotamento de tupla.
>>> a, b, c
(1, 2, 3)
>>> list((1, 2, 3))  # Converte uma tupla para lista.
[1, 2, 3]
>>> tuple([4, 5, 6])  # Converte uma lista para tupla.
(4, 5, 6)
```

#### Tuplas em ação

Talvez a melhor maneira de entender as tuplas seja vê-las em funcionamento. Vamos, mais uma vez exemplificar algumas interações do interpretador, para ilustrar as operações da tabela 1.3

```python
>>> T = (1, 2, 3, 4) # Criar uma tupla
>>> T
(1, 2, 3, 4)
>>> # Indexação (acessar elemento pelo índice)
>>> T[0]
1
>>> # Fatiamento (slice) retorna parte da tupla
>>> T[1:3]
(2, 3)
>>> 
>>> T[0], T[1:3] # Acessar múltiplos ao mesmo tempo (indexação + slice)
(1, (2, 3))
>>> 
>>> (1, 2) + (3, 4) # Concatenação de tuplas
(1, 2, 3, 4)
>>> 
>>> (1, 2) * 4 # Repetição dos elementos
(1, 2, 1, 2, 1, 2, 1, 2)
>>> 
>>> 3 in T # Verificar se um elemento está presente
True
>>> 
>>> len(T) # Comprimento da tupla
4
>>> 
>>> T.count(2) # Contar quantas vezes um elemento aparece
1
>>> 
>>> T.index(3) # Encontrar o índice da primeira ocorrência
2
>>> 
>>> a, b, c, d = T # Desempacotamento da tupla em variáveis
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> 
>>> x = (1,) # Tupla de um único elemento (necessário usar vírgula)
>>> x
(1,)
>>> 
>>> list(T) # Converter tupla para lista
[1, 2, 3, 4]
>>> 
>>> tuple([1, 2, 3]) # Converter lista para tupla
(1, 2, 3)
```

Vale a pena consultar documentação e livros técnicos para se aprofundar no assunto.

