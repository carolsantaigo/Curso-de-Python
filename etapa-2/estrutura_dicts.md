# Fundamentos de Python (Tipos Compostos) parte 1

## Listas e Dicionários

Agora vamos explorar um pouco mais a fundo os tipos compostos do Python, coleções de objetos que são os principais componentes em quase todos os scripts em Python.

Conforme veremos, esses tipos são notavelmente flexíveis: eles podem ser alterados, podem aumentar e diminuir segundo a demanda e podem conter e serem aninhados em qualquer outro tipo de objetos. Usando bem esses tipos, podemos construir e processar estruturas de informação arbitrariamente ricas em nossos scripts.

### Listas

As listas representam o tipo de objeto coleção ordenado mais flexível do Python. Ao contrário das strings, as listas podem conter qualquer tipo de objeto: números, strings e até outras listas. As listas do Python fazem o trabalho da maioria das estruturas de dados tipo coleção.

Em termos, algumas as propriedades principais das listas do Python são:

* *Coleções ordenadas de objetos arbitrários*

* *Acessadas pelo deslocamento*

* *Têm comprimento variável, são heterogêneas e podem ser aninhadas arbitrariamente*

* *Categoria sequência mutável*

* *Arrays de referência de objeto*

## Operações Comuns com Listas em Python

*Tabela 1.1*

| Operação                        | Exemplo                          | Descrição                                            |
| ------------------------------- | -------------------------------- |:---------------------------------------------------- |
| Criar uma lista                 | `lista = [1, 2, 3]`              | Cria uma lista com elementos.                        |
| Acessar elemento por índice     | `lista[0]`                       | Retorna o primeiro elemento.                         |
| Alterar elemento                | `lista[1] = 42`                  | Modifica o valor de um elemento.                     |
| Adicionar no final              | `lista.append(4)`                | Adiciona um elemento ao final.                       |
| Adicionar em posição específica | `lista.insert(1, 99)`            | Insere um elemento na posição indicada.              |
| Concatenar listas               | `lista + [5, 6]`                 | Cria uma nova lista concatenada.                     |
| Remover por valor               | `lista.remove(2)`                | Remove o primeiro elemento com o valor especificado. |
| Remover por índice              | `del lista[0]` ou `lista.pop(0)` | Remove o elemento na posição indicada.               |
| Obter tamanho                   | `len(lista)`                     | Retorna a quantidade de elementos.                   |
| Verificar existência            | `3 in lista`                     | Retorna `True` se o valor está na lista.             |
| Ordenar lista                   | `lista.sort()`                   | Ordena a lista em ordem crescente.                   |
| Ordenar sem alterar original    | `sorted(lista)`                  | Retorna uma nova lista ordenada.                     |
| Inverter ordem                  | `lista.reverse()`                | Inverte a ordem da lista.                            |
| Copiar lista                    | `copia = lista.copy()`           | Cria uma cópia rasa (shallow copy).                  |
| Limpar lista                    | `lista.clear()`                  | Remove todos os elementos da lista.                  |
| Fatiar lista                    | `lista[1:3]`                     | Retorna uma sublista do índice 1 ao 2.               |
| Iterar sobre elementos          | `for item in lista: ...`         | Percorre todos os elementos.                         |

Quando escritas, as listas são codificadas como uma série de objetos (ou expressões que retornam objetos) entre colchetes, separadas por vírgula. Use seu interpretador Python e veja a saída:

```python
>>> lista = [1, 2, 3] #cria uma lista de 3 posições.
>>> lista
[1, 2, 3]
```

### Listas em Ação

Talvez a melhor maneira de entender as listas seja vê-las em funcionamento. Vamos, mais uma vez, exemplificar algumas interações simples do interpretador, para ilustrar as operações da tabela 1.1.

```python
>>> lista = [1, 2, 3]  # Cria uma lista
>>> len(lista)  # Consulta o comprimento da lista
3

>>> [1, 2, 3] + [4, 5, 6]  # Concatena duas listas
[1, 2, 3, 4, 5, 6]

>>> ['Python'] * 3  # Repete 3 vezes o conteúdo da lista
['Python', 'Python', 'Python']

>>> 3 in lista  # Verifica se o elemento está na lista
True

>>> for x in lista: 
...     print(x)  # Itera sobre a lista
...
1
2
3

>>> lista.append(4)  # Adiciona um elemento ao final
>>> lista
[1, 2, 3, 4]

>>> lista.insert(1, 99)  # Insere 99 na posição 1
>>> lista
[1, 99, 2, 3, 4]

>>> lista.remove(99)  # Remove o elemento 99
>>> lista
[1, 2, 3, 4]

>>> lista.pop()  # Remove e retorna o último elemento
4
>>> lista
[1, 2, 3]

>>> lista[::-1]  # Retorna a lista invertida (fatiamento)
[3, 2, 1]

>>> sorted([3, 1, 2])  # Retorna uma nova lista ordenada
[1, 2, 3]

>>> lista.clear()  # Remove todos os elementos
>>> lista
[]

```

#### Indexação, fracionamento e matrizes

Como listas são seqüências, a indexação e o fracionamento funcionam da mesma maneira, mas o resultado da indexação de uma lista depende do tipo de objeto que está no deslocamento especificado, e o fracionamento de uma lista sempre retorna uma nova lista:

```python
>>> lista = [10, 20, 30, 40, 50] # Criando uma lista simples
>>> lista[0]  # INDEXAÇÃO (acessa um elemento específico)
10
>>> lista[-1]  # último elemento
50
>>> lista[1:4]  # FRACIONAMENTO (fatiamento) – sempre retorna uma NOVA lista
[20, 30, 40]
>>> lista[:3]  # do início até o índice 2
[10, 20, 30]
>>> lista[2:]  # do índice 2 até o fim
[30, 40, 50]
>>> lista[:]  # cópia rasa da lista
[10, 20, 30, 40, 50]
>>> lista[::2]  # de 2 em 2 elementos
[10, 30, 50]
>>> lista[::-1]  # inverte a lista
[50, 40, 30, 20, 10]
>>> 
>>> matriz = [ # LISTAS ANINHADAS (MATRIZES)
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>> 
>>> matriz[0] # Acessando uma linha inteira
[1, 2, 3]
>>> 
>>> matriz[1][2] # Acessando um elemento específico (linha 1, coluna 2)
6
>>> 
>>> [linha[0] for linha in matriz] # Pegando apenas a primeira coluna (com list comprehension)
[1, 4, 7]
>>>
>>> [linha[1:] for linha in matriz]  # Pegando um "sub-bloco" com fatiamento
[[2, 3], [5, 6], [8, 9]]
```

Dá para se fazer muita coisa com Listas, recomendo criar um arquivo `.py` e testar formas diferentes de trabalhar com elas. O assunto sobre listas e bem grande e vale a pena consultar sua documentação em:

## Dicionários

Além das listas, os *dicionários* talvez sejam o tipo de dados interno mais flexível no Python. Se você considera as listas como coleções ordenadas de objetos, os dicionários são coleções desordenadas; a principal diferença é que, nos dicionários, os itens são armazenados e buscados pela *chave*, em vez do deslocamento posicional.

Sendo um tipo interno, os dicionários podem substituir muitos dos algoritmos de pesquisa e estrutura de dados que talvez tenham que ser implementados manualmente em linguagens de nível mais abaixo (Assembly, C e, em alguns casos, C++ são consideradas linguagens de baixo nível) - indexar um dicionário é uma operação de pesquisa muito rápida. Às vezes, os dicionários fazem o trabalho de registros e tabelas de símbolos usados em outras linguagens (JSON pode ser um exemplo), podem representar estruturas de dados esparsas (principalmente vazias) e muito mais.

Com referência às suas principais propriedades, os dicionários são:

* *Acessados pela chave e não pelo deslocamento*

* *Coleções desordenadas de objetos arbitrários*

* *Têm comprimento variável, são heterogêneos e podem ser aninhados arbitrariamente*

* *Categoria mutável mapeamento*

* *Tabelas de referências de objeto (tabelas de hashing)*

*Tabela 1.2*

## Operações Comuns com Dicionários no Python

| Operação                      | Exemplo                       | Descrição                                       |
| ----------------------------- | ----------------------------- | ----------------------------------------------- |
| **Criar um dicionário**       | `d = {"a": 1, "b": 2}`        | Cria um dicionário com chaves e valores         |
| **Acessar valor por chave**   | `d["a"]`                      | Retorna o valor associado à chave `"a"`         |
| **Adicionar/Atualizar valor** | `d["c"] = 3`                  | Adiciona nova chave ou atualiza valor existente |
| **Remover chave/valor**       | `del d["a"]`                  | Remove o par `"a": 1` do dicionário             |
| **Remover e retornar valor**  | `d.pop("b")`                  | Remove a chave e retorna o valor                |
| **Obter valor com padrão**    | `d.get("x", 0)`               | Retorna `0` se a chave não existir              |
| **Listar chaves**             | `d.keys()`                    | Retorna uma *view* com as chaves                |
| **Listar valores**            | `d.values()`                  | Retorna uma *view* com os valores               |
| **Listar itens**              | `d.items()`                   | Retorna pares `(chave, valor)`                  |
| **Verificar chave**           | `"a" in d`                    | Retorna `True` se a chave existe                |
| **Mesclar dicionários**       | `d.update({"x": 10})`         | Adiciona/atualiza chaves de outro dicionário    |
| **Copiar dicionário**         | `copia = d.copy()`            | Cria uma cópia rasa (*shallow copy*)            |
| **Limpar dicionário**         | `d.clear()`                   | Remove todos os itens                           |
| **Criar com chaves fixas**    | `dict.fromkeys(["a","b"], 0)` | Cria com chaves específicas e valor padrão      |
| **Comprimento**               | `len(d)`                      | Retorna a quantidade de itens                   |

Os dicionários são escritos como uma série de pares chave:valor, separados por vírgula e incluídos entre chaves. Freqüêntemente, os dicionários são construídos pela atribuição a novas chaves em tempo de execução, em vez da gravação de literais. Mas veja a seção a seguir, sobre alteração em dicionários; as listas e os dicionários crescem de maneiras diferentes. A atribuição a novas chaves funciona para dicionários, mas falha para listas (em vez disso, as listas crescem com `append`).

Use seu interpretador Python e veja a saída:

```python
>>> d2 = {'spam': 2, 'ham': 1, 'eggs': 3} # Cria um dicionário.
>>> d2['spam'] #Busca valor pela chave.
2
>>> d2 # A ordem é misturada.
{'spam': 2, 'ham': 1, 'eggs': 3}
>>>
```

### Dicionários em ação

Conforme a tabela 1.2 sugere, os dicionários são indexados pela chave e as entradas de dicionário aninhadas são referenciadas por uma série de índices (chave entre colchetes). Quando o Python cria um dicionário, ele armazena seus itens em qualquer ordem que escolher; para buscar um valor de volta, forneça a chave a que ele está associado.

```python
>>> d2 = {'spam': 1, 'ham': 2, 'eggs': 3}
>>> len(d2)           # Número de entradas no dicionário
3
>>> 'ham' in d2       # Teste de participação da chave como membro
True
>>> d2.keys()         # View com as chaves do dicionário
dict_keys(['spam', 'ham', 'eggs'])
>>> list(d2.keys())   # Converter para lista
['spam', 'ham', 'eggs']
>>> d2.values()       # View com os valores
dict_values([1, 2, 3])
>>> d2.items()        # Pares (chave, valor)
dict_items([('spam', 1), ('ham', 2), ('eggs', 3)])


```

#### Uma tabela de linguagens

Aqui está um exemplo de dicionário mais realista. O exemplo a seguir cria uma tabela que faz o mapeamento de nomes de linguagens de programação (as chaves) para seus criadores (os valores). Você busca o nome de um criador indexando no nome da linguagem:

```python
>>> table = { # Acessando valores e percorrendo dicionários
...     'Python': 'Guido van Rossum',
...     'perl': 'Larry Wall',
...     'Tc1': 'jhon Ousterhout'
... }
>>> language = 'Python'
>>> creator = table[language]   # Acessando diretamente pelo nome da chave
>>> creator
'Guido van Rossum'
>>> for lang in table.keys(): # Iterando apenas pelas chaves e acessando os valores
...     print(f'{lang}\t{table[lang]}')
...
Python  Guido van Rossum
perl    Larry Wall
Tc1     jhon Ousterhout
>>> for chave, valor in table.items(): # Iterando diretamente em chave e valor com items()
...     print(f'{chave} - {valor}')
...
Python - Guido van Rossum
perl - Larry Wall
Tc1 - jhon Ousterhout
```

Esse também é um assunto que renderia muitas páginas e discusões, mas vale a pena verificar a documentação, como sempre ela será sua melhor companheira.

### *Referências Biográficas*

:link: [Documentação do Python sobre Listas]([5. Estruturas de dados &#8212; Documentação Python 3.13.5](https://docs.python.org/pt-br/3.13/tutorial/datastructures.html))

:link: [Documentação do Python sobre Dicionários](https://docs.python.org/pt-br/3/library/stdtypes.html#dict)

:books: [Curso Intensivo de Python* – 2ª Edição, Eric Matthes](https://www.amazon.com.br/Curso-Intensivo-Python-Introdu%C3%A7%C3%A3o-Programa%C3%A7%C3%A3o/dp/8575228439/ref=asc_df_8575228439?mcid=33d3b3f47f803393b5d6cc7020a3f52f&tag=googleshopp00-20&linkCode=df0&hvadid=709884550309&hvpos=&hvnetw=g&hvrand=1595147511137249852&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9212131&hvtargid=pla-2201383736059&psc=1&language=pt_BR&gad_source=1)

:books: [Aprendendo Python* – 2ª Edição, Mark Lutz & David Ascher](https://www.amazon.com.br/Aprendendo-Python-David-Ascher/dp/857780013X/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9R6928TG789E&dib=eyJ2IjoiMSJ9.LY5V4N2CPb3oKhtV_Fiu13xmw2sBInVC5DMnfx7ipT2l-H6b5jp3M3ndJStYAzFYZ75lQ3qpq75pIxXlVtYgKWOuSm34eVAwKV308rxusy2EPtJjLS-BmellKR1FXicXIoKmD7v0kz3KqTpa_bBmg-QkdcKzP08DMnKjibJ3GnTUr0DRsKlWFVblvkKuNJ9Lsv6sy5GcR10mVGUt1xhsDpX-BM3ONbvBuc-pQkHoYq8.eC6ZeUGmJJYrrrxVIoNdQXQUOp6Y3kQfnbZylu-WB7M&dib_tag=se&keywords=aprendendo+Python&qid=1752933061&s=books&sprefix=aprendendo+python%2Cstripbooks%2C194&sr=1-2)

## Licença & Autoria

📄 Este material é de autoria de **[Thiago Povoa](https://github.com/devpovoa)** e pode ser utilizado livremente para fins de estudo.  
Caso utilize em outro projeto, mantenha a referência ao autor.  
