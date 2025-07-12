# Entrada e saída de dados

## O que são?

Em Python, usamos:

- `input()` para **receber dados do usuário**.
- `print()` para **exibir mensagens e valores** no terminal.

Essas duas funções são fundamentais para a interação com o usuário.

---

### Exemplo de entrada com `input()`

```python
nome = input("Digite seu nome: ")  # o que o usuário digitar será armazenado na variável
```
O valor retornado por input() é sempre do tipo str (string), mesmo que pareça um número.

### Exemplo de saída com `print()`
```python
print("Olá, mundo!")  # exibe uma mensagem fixa no terminal
```

Você pode imprimir textos, variáveis e até expressões matemáticas:

```python
idade = 30
print("Idade:", idade)
print("5 + 3 =", 5 + 3)
```
### Exemplo combinado: recebendo e exibindo dados
```python
nome = input("Qual seu nome? ")
print("Bem-vindo(a),", nome)
```

### Conversão de tipos com `input()`
Como input() sempre retorna uma string, para trabalhar com números é necessário converter:
```python 
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```
### Dica: pulando linha ou usando separadores
```python
print("Olá", "mundo", sep=" - ")  # Olá - mundo
print("Linha 1")
print("Linha 2")  # quebra de linha automática
```