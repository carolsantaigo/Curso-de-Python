# Fundamentos de Python (Funções) – Parte 1

## Introdução às Funções

Funções são blocos nomeados de código que realizam tarefas específicas. Em Python, são declaradas com a palavra-chave `def` e servem para:

- **Evitar repetição de código**
- **Organizar o programa em partes reutilizáveis**
- **Facilitar a leitura, testes e manutenção**

### Características

- Podem receber parâmetros
- Podem ou não retornar valores
- Executam apenas quando chamadas
- Melhoram a modularização do código

---

## Sintaxe de uma função

```python
def nome_da_funcao():
    # bloco indentado de código
    pass
```

---

## Exemplo simples

```python
def saudacao():
    print("Olá, bem-vindo ao curso de Python!")

saudacao()
```

> Saída:
>
> Olá, bem-vindo ao curso de Python!

---

## Funções sem retorno

Funções podem ser criadas apenas para executar ações:

```python
def mostrar_menu():
    print("1 - Iniciar")
    print("2 - Sair")

mostrar_menu()
```

---

## Corpo vazio: `pass`

Use `pass` para criar uma função cujo corpo será definido depois:

```python
def recurso_em_construcao():
    pass
```

---

## Boas práticas ao criar funções

- Use nomes descritivos e verbos (ex: `calcular_total()`)
- Evite que uma função faça mais de uma coisa
- Prefira funções curtas e reutilizáveis

---

## Exemplo passo a passo

```python
>>> def somar():
...     print(2 + 3)
...
>>> somar()
5
```
