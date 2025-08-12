# Leitura e Escrita de Arquivos em Python

## Abrindo Arquivos

A função `open()` é usada para abrir arquivos. É recomendado usar o gerenciador de contexto (`with`).

```python
# Modos de abertura:
# 'r' - leitura (padrão)
# 'w' - escrita (sobrescreve o arquivo existente)
# 'a' - anexar (adiciona ao final do arquivo)
# 'b' - modo binário
# '+' - leitura e escrita

# Abrindo para leitura (modo padrão)
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
```

## Lendo Arquivos

### Leitura Completa
```python
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()  # Lê todo o conteúdo
    print(conteudo)
```

### Leitura Linha por Linha
```python
with open('exemplo.txt', 'r') as arquivo:
    for linha in arquivo:  # Lê uma linha por vez
        print(linha.strip())  # strip() remove \n no final
```

### Lendo Todas as Linhas em uma Lista
```python
with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()  # Retorna uma lista de linhas
    for linha in linhas:
        print(f"Linha: {linha.strip()}")
```

### Lendo uma Quantidade Específica de Caracteres
```python
with open('exemplo.txt', 'r') as arquivo:
    pedaco = arquivo.read(100)  # Lê os primeiros 100 caracteres
    print(pedaco)
```

## Escrevendo em Arquivos

### Sobrescrevendo um Arquivo
```python
with open('saida.txt', 'w') as arquivo:
    arquivo.write('Primeira linha\n')
    arquivo.write('Segunda linha\n')
    arquivo.writelines(['Terceira linha\n', 'Quarta linha\n'])
```

### Anexando a um Arquivo
```python
with open('saida.txt', 'a') as arquivo:
    arquivo.write('Nova linha adicionada\n')
```

## Trabalhando com Caminhos de Arquivo

```python
import os

# Juntando caminhos de forma segura
caminho = os.path.join('pasta', 'subpasta', 'arquivo.txt')
print(caminho)  # pasta/subpasta/arquivo.txt (ou pasta\subpasta\arquivo.txt no Windows)

# Obtendo o diretório atual
diretorio_atual = os.getcwd()
print(diretorio_atual)

# Verificando se um arquivo existe
if os.path.exists('arquivo.txt'):
    print("O arquivo existe!")

# Verificando se é um arquivo ou diretório
print(os.path.isfile('arquivo.txt'))  # True
print(os.path.isdir('pasta'))        # True
```

## Gerenciamento de Arquivos Temporários

```python
import tempfile

# Criando um arquivo temporário
with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp:
    tmp.write(b'Conteúdo temporário')
    print(f"Arquivo temporário criado em: {tmp.name}")
    # O arquivo será removido automaticamente ao sair do bloco 'with'
```

## Boas Práticas

1. **Sempre** use o gerenciador de contexto (`with`) para garantir que o arquivo seja fechado corretamente.
2. Especifique a codificação (geralmente 'utf-8') ao trabalhar com texto.
3. Use `os.path` para manipular caminhos de forma portável.
4. Verifique se o arquivo existe antes de tentar abri-lo para leitura.
5. Lide com exceções ao trabalhar com arquivos.

## Exemplo Completo com Tratamento de Erros

```python
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return None
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo {nome_arquivo}.")
        return None
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo: {e}")
        return None
```

## Exercícios

1. Crie uma função que conte quantas vezes cada palavra aparece em um arquivo de texto.
2. Implemente um programa que copie o conteúdo de um arquivo para outro, mas invertendo a ordem das linhas.
3. Escreva um programa que leia um arquivo CSV e exiba o conteúdo formatado como uma tabela.
4. Crie um programa de backup que copie todos os arquivos .txt de um diretório para outro.
5. Implemente um sistema de log que registre mensagens com data e hora em um arquivo.
