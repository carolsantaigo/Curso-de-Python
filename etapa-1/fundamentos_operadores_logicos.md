# Operadores lógicos

## O que são?

Operadores lógicos são usados para **combinar expressões booleanas** (que resultam em `True` ou `False`). Em Python, temos três operadores principais.

---

## Operador `and`

Retorna `True` se **ambas** as expressões forem verdadeiras.

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
# Resultado: Pode dirigir
```

### Operador `or`
Retorna True se pelo menos uma das expressões for verdadeira.
```python
tem_dinheiro = False
tem_cartao = True

if tem_dinheiro or tem_cartao:
    print("Pode fazer a compra")
# Resultado: Pode fazer a compra
```

### Operador `not`
Inverte o valor lógico da expressão.
```python
logado = False

if not logado:
    print("Usuário precisa fazer login")
# Resultado: Usuário precisa fazer login
```