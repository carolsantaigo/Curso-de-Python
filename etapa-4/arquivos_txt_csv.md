# Manipulação de Arquivos .txt e .csv em Python

## Trabalhando com Arquivos de Texto (.txt)

### Leitura Básica
```python
# Lendo um arquivo de texto inteiro
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo linha por linha
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

### Processando Dados de Texto
```python
# Contando palavras em um arquivo
def contar_palavras(arquivo_nome):
    contador = {}
    with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.strip().split()
            for palavra in palavras:
                palavra = palavra.lower().strip('.,!?;:')
                if palavra:
                    contador[palavra] = contador.get(palavra, 0) + 1
    return contador
```

## Trabalhando com Arquivos CSV

### Usando o Módulo csv
```python
import csv

# Lendo um arquivo CSV
with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        print(linha)  # Cada linha é uma lista de valores

# Lendo para um dicionário
with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for registro in leitor:
        print(registro)  # Cada registro é um dicionário
```

### Escrevendo em CSV
```python
# Escrevendo uma lista de listas
with open('saida.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalho
    escritor.writerow(['João', '30', 'São Paulo'])
    escritor.writerow(['Maria', '25', 'Rio de Janeiro'])

# Escrevendo um dicionário
dados = [
    {'nome': 'João', 'idade': '30', 'cidade': 'São Paulo'},
    {'nome': 'Maria', 'idade': '25', 'cidade': 'Rio de Janeiro'}
]

with open('saida_dict.csv', 'w', newline='', encoding='utf-8') as arquivo:
    campos = ['nome', 'idade', 'cidade']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(dados)
```

## Processando Arquivos Grandes

### Leitura em Blocos
```python
def processar_arquivo_grande(arquivo_nome, tamanho_bloco=8192):
    with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
        while True:
            bloco = arquivo.read(tamanho_bloco)
            if not bloco:
                break
            # Processa o bloco aqui
            yield bloco
```

### Usando pandas para CSV
```python
import pandas as pd

# Lendo um CSV com pandas
df = pd.read_csv('dados.csv')
print(df.head())  # Mostra as primeiras linhas

# Filtrando dados
filtrado = df[df['idade'] > 25]

# Salvando para CSV
filtrado.to_csv('filtrado.csv', index=False)
```

## Exemplo Prático: Processador de Dados CSV

```python
import csv
from collections import defaultdict

def processar_vendas(arquivo_entrada, arquivo_saida):
    # Dicionário para armazenar totais por produto
    totais = defaultdict(float)
    
    # Lendo o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as entrada:
        leitor = csv.DictReader(entrada)
        
        # Processando cada linha
        for linha in leitor:
            produto = linha['produto']
            quantidade = int(linha['quantidade'])
            preco = float(linha['preco_unitario'])
            
            # Atualizando o total do produto
            totais[produto] += quantidade * preco
    
    # Escrevendo o relatório
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as saida:
        campos = ['produto', 'total_vendido']
        escritor = csv.DictWriter(saida, fieldnames=campos)
        
        escritor.writeheader()
        for produto, total in totais.items():
            escritor.writerow({
                'produto': produto,
                'total_vendido': f"{total:.2f}"
            })

# Exemplo de uso
processar_vendas('vendas.csv', 'relatorio_vendas.csv')
```

## Boas Práticas

1. **Sempre** feche os arquivos após o uso (use `with`).
2. Especifique a codificação correta (geralmente 'utf-8').
3. Use `newline=''` ao trabalhar com arquivos CSV no Windows.
4. Para arquivos grandes, processe linha por linha ou em blocos.
5. Valide os dados antes de processá-los.
6. Use o módulo `csv` em vez de manipular strings manualmente.
7. Faça backup dos arquivos originais antes de processá-los.

## Exercícios

1. Crie um programa que leia um arquivo de log e conte quantas vezes cada tipo de erro ocorreu.
2. Implemente um conversor de CSV para JSON.
3. Crie um programa que combine dados de vários arquivos CSV em um único arquivo.
4. Escreva um validador de arquivos CSV que verifique se todas as linhas têm o mesmo número de campos.
5. Implemente um programa que leia um grande arquivo de texto e gere um índice de palavras com as linhas onde cada palavra aparece.
