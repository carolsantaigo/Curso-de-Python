# Estruturas condicionais

## O que são?

Estruturas condicionais permitem que o programa **tome decisões** com base em condições. Em Python, utilizamos os comandos `if`, `elif` e `else` para definir esses fluxos.

---

## Sintaxe básica

```python
if condição:
    # bloco executado se a condição for verdadeira
elif outra_condição:
    # bloco executado se a primeira for falsa e essa for verdadeira
else:
    # bloco executado se todas as anteriores forem falsas
```

### Exemplo com `if`
```python
idade = 20

if idade >= 18:
    print("Você é maior de idade")
```

### Exemplo com `if` e `else`

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Exemplo com `if`, `elif` e `else`

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

```
### Operadores usados com condicionais

| Operador 	| Significado    	| Exemplo 	|
|----------	|----------------	|---------	|
| ==       	| igual a        	| a == b  	|
| !=       	| diferente de   	| a != b  	|
| >        	| maior que      	| a > b   	|
| <        	| menor que      	| a < b   	|
| >=       	| maior ou igual 	| a >= b  	|
| <=       	| menor ou igual 	| a <= b  	|

### Condições compostas com operadores lógicos
Você pode combinar múltiplas condições com `and`, `or`, `not`.

```python
idade = 25
habilitacao = True

if idade >= 18 and habilitacao:
    print("Pode dirigir")
```


```python
```