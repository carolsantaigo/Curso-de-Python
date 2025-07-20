## Conjuntos (Set)

Outro tipo de objeto básico do Python é o _set_ (conjunto), que representa uma coleção **não ordenada** e **sem elementos duplicados**. Os conjuntos são úteis para testar **pertinência** (verificar se um elemento está presente), **remover duplicatas** e **realizar operações matemáticas de conjuntos**, como união, interseção e diferença.

Ao contrário das listas e tuplas, os conjuntos **não mantêm ordem** dos elementos e não são indexáveis. Eles são implementados como uma tabela hash e, portanto, têm busca muito eficiente.

Os conjuntos:

* _São coleções não ordenadas de objetos únicos_

* _Não possuem índices nem fatiamento (slice)_

* _São mutáveis (mas só podem conter objetos imutáveis como elementos)_

* _Suportam operações matemáticas típicas de teoria dos conjuntos (união, interseção, diferença)_

* _Não permitem elementos duplicados_

Existem dois tipos de conjunto em Python:

* **set**: conjunto mutável, que permite adicionar ou remover elementos.

* **frozenset**: conjunto **imutável**, que não pode ser modificado após criado.

Operações comuns com Sets no Python
-----------------------------------

_Tabela 1.4_

| Operação                    | Exemplo          | Descrição                                           |
| --------------------------- | ---------------- | --------------------------------------------------- |
| Criar um set                | `s = {1, 2, 3}`  | Declaração simples de um conjunto.                  |
| Criar set vazio             | `s = set()`      | Conjunto vazio (não pode usar `{}` pois cria dict). |
| Adicionar elemento          | `s.add(4)`       | Adiciona um elemento ao conjunto.                   |
| Remover elemento            | `s.remove(2)`    | Remove um elemento (gera erro se não existir).      |
| Descartar elemento          | `s.discard(5)`   | Remove se existir (não gera erro).                  |
| Limpar conjunto             | `s.clear()`      | Remove todos os elementos.                          |
| Verificar elemento          | `3 in s`         | Checa se um elemento está presente.                 |
| União                       | `s1              | s2`                                                 |
| Interseção                  | `s1 & s2`        | Retorna a interseção dos conjuntos.                 |
| Diferença                   | `s1 - s2`        | Retorna os elementos de s1 que não estão em s2.     |
| Diferença simétrica         | `s1 ^ s2`        | Retorna elementos exclusivos de cada conjunto.      |
| Comprimento                 | `len(s)`         | Retorna a quantidade de elementos.                  |
| Converter para lista        | `list(s)`        | Converte o conjunto em uma lista.                   |
| Remover duplicatas de lista | `set([1,2,2,3])` | Conjunto elimina duplicatas automaticamente.        |
| Congelar conjunto           | `frozenset(s)`   | Cria um conjunto imutável.                          |

Os conjuntos são escritos como uma série de objetos separados por vírgula, incluídos entre **chaves `{}`**, ou criados com a função `set()`. Use seu interpretador Python e veja a saída da no terminal sobre a tabela 1.4:

```python
>>> s = {1, 2, 3}  # Criar um conjunto
>>> s
{1, 2, 3}
>>> s.add(4)  # Adicionar elemento
>>> s
{1, 2, 3, 4}
>>> s.remove(2)  # Remover elemento (gera erro se não existir)
>>> s
{1, 3, 4}
>>> s.discard(10)  # Descartar elemento (não gera erro)
>>> s
{1, 3, 4}
>>> 3 in s  # Verificar se elemento está presente
True
>>> len(s)  # Quantidade de elementos
3
>>> list(s)  # Converter conjunto para lista
[1, 3, 4]
>>> set([1,2,2,3])  # Remover duplicatas automaticamente
{1, 2, 3}
```

Não podemos deixar de fazer sobre o frozenset:

```python
>>> s = {1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> fs = frozenset([1, 2, 3])
>>> fs
frozenset({1, 2, 3})
>>> fs.add(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
```

Esse conjuto é imutável e não possui métodos que alterem seu conteúdo. Novamente esse é um assunto que renderia muitas páginas e discurões, mas vale a pena verificar a documentação.

### *Referências Biográficas*

:link: [Documentação do Ptyhon sobre tuplas](https://docs.python.org/pt-br/3.13/c-api/tuple.html)

:link: [Documentação do Ptyhon sobre set](https://docs.python.org/pt-br/3.13/c-api/set.html)

:books: [Learning Python: Powerful Object-Oriented Programming](https://www.amazon.com.br/Learning-Python-Mark-Lutz/dp/1449355730/ref=asc_df_1449355730?mcid=825133ff5e4f3d839689e96f04d33f59&tag=googleshopp00-20&linkCode=df0&hvadid=709883381671&hvpos=&hvnetw=g&hvrand=14341478298000667061&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9212131&hvtargid=pla-404766166559&psc=1&language=pt_BR&gad_source=1)

:books: [Curso Intensivo de Python* – 2ª Edição, Eric Matthes](https://www.amazon.com.br/Curso-Intensivo-Python-Introdu%C3%A7%C3%A3o-Programa%C3%A7%C3%A3o/dp/8575228439/ref=asc_df_8575228439?mcid=33d3b3f47f803393b5d6cc7020a3f52f&tag=googleshopp00-20&linkCode=df0&hvadid=709884550309&hvpos=&hvnetw=g&hvrand=1595147511137249852&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9212131&hvtargid=pla-2201383736059&psc=1&language=pt_BR&gad_source=1)

## Licença & Autoria

📄 Este material é de autoria de **[Thiago Povoa](https://github.com/devpovoa)** e pode ser utilizado livremente para fins de estudo.Caso utilize em outro projeto, mantenha a referência ao autor.


