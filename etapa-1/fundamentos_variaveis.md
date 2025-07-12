# Variáveis

## O que são variáveis?

Variáveis são **nomes que armazenam dados** na memória do computador. Em Python, você não precisa declarar o tipo da variável — ele é definido automaticamente conforme o valor atribuído.

**Sintaxe:**
```python
nome_variavel = valor
```

## Exemplos de variáveis por tipo
### Tipo int (número inteiro)
```python
idade = 25        # idade da pessoa
quantidade = -3   # quantidade negativa
saldo = 0         # saldo zerado
```

### Tipo float (número com ponto decimal)
```python
altura = 1.75        # altura em metros
preco = 9.99         # valor monetário
temperatura = -2.5   # temperatura negativa
```

### Tipo bool (valor lógico)
```python
ativo = True     # usuário está ativo
pago = False     # pagamento ainda não realizado
```
### Tipo str (texto)
```python
nome = "Ana"                     # nome próprio
mensagem = 'Olá, mundo!'         # saudação
codigo = "12345"                 # código como texto
```

### Tipo list (lista mutável)
```python
notas = [8, 9.5, 10]                 # lista de notas
nomes = ["João", "Maria", "Pedro"]   # lista de nomes
```
### Tipo tuple (tupla imutável)
```python
coordenadas = (10.5, 20.3)              # posição no mapa
cores = ("vermelho", "verde", "azul")   # cores primárias
```

### Tipo set (conjunto sem repetição)
```python
numeros_unicos = {1, 2, 3}     # conjunto de inteiros
letras = {"a", "b", "c"}       # conjunto de letras
```

### Tipo dict (dicionário chave:valor)
```python
usuario = {"nome": "Carlos", "idade": 30}      # dados de um usuário
produto = {"id": 123, "preco": 19.90}          # informações de produto
```

### Tipo NoneType (ausência de valor)
```python
resposta = None     # valor indefinido ou nulo
```

### Tipo bytes e bytearray (dados binários)
Obs: resolve boa parte dos problemas com UTF-8
```python
dados = b"texto em bytes"             # bytes imutáveis
dados_mutaveis = bytearray(b"abc")    # bytes mutáveis
```