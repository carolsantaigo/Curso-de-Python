# Exercícios - Manipulação de Strings e Arquivos

## Exercícios Básicos

### 1. Contador de Palavras
Escreva uma função que receba o caminho de um arquivo de texto e retorne um dicionário com a contagem de cada palavra no arquivo (ignorando maiúsculas/minúsculas e pontuação).

### 2. Conversor CSV para JSON
Crie um programa que leia um arquivo CSV e o converta para o formato JSON. O programa deve aceitar os parâmetros de entrada e saída pela linha de comando.

### 3. Buscador de Arquivos
Implemente uma função que receba um diretório e uma palavra-chave, e retorne uma lista com os nomes dos arquivos que contêm aquela palavra.

### 4. Validador de E-mails
Escreva uma função que leia um arquivo de texto e retorne todos os endereços de e-mail válidos encontrados, usando expressões regulares.

## Exercícios Intermediários

### 5. Log Parser
Crie um programa que analise um arquivo de log e gere um relatório com:
- Número total de erros, avisos e mensagens informativas
- As 5 mensagens de erro mais frequentes
- Distribuição de mensagens por hora do dia

### 6. Compactador de Arquivos
Implemente um programa que leia um diretório, compacte todos os arquivos de texto em um único arquivo ZIP, mantendo a estrutura de diretórios.

### 7. Conversor de Codificação
Escreva um programa que converta a codificação de todos os arquivos .txt em um diretório de ISO-8859-1 para UTF-8.

## Exercícios Avançados

### 8. Análise de Dados de Vendas
Dado um arquivo CSV com dados de vendas (data, produto, quantidade, valor), crie um programa que:
- Calcule o total de vendas por produto
- Identifique o produto mais vendido
- Gere um relatório em formato Markdown com as análises

### 9. Web Scraper para Arquivos
Crie um programa que:
1. Leia uma lista de URLs de um arquivo
2. Baixe o conteúdo de cada URL
3. Extraia todos os links e imagens
4. Salve as informações em um arquivo JSON estruturado

### 10. Processador de Templates
Implemente um sistema de templates que:
- Leia um arquivo de template com placeholders (ex: `{nome}`)
- Leia um arquivo CSV com os dados
- Gere um arquivo de saída para cada linha do CSV, substituindo os placeholders

## Projeto Final

### Sistema de Gerenciamento de Tarefas
Crie um aplicativo de linha de comando para gerenciar tarefas com os seguintes requisitos:

1. **Armazenamento**:
   - As tarefas devem ser salvas em um arquivo JSON
   - Cada tarefa deve ter: ID, título, descrição, data de criação, data de conclusão e status

2. **Funcionalidades**:
   - Adicionar nova tarefa
   - Listar todas as tarefas (com opções de filtro por status)
   - Marcar tarefa como concluída
   - Remover tarefa
   - Buscar tarefas por palavra-chave
   - Exportar tarefas para CSV
   - Importar tarefas de um arquivo CSV

3. **Interface**:
   - Use `argparse` para criar uma interface de linha de comando amigável
   - Inclua ajuda detalhada para cada comando
   - Formate a saída de forma legível

4. **Tratamento de Erros**:
   - Valide todas as entradas do usuário
   - Forneça mensagens de erro claras
   - Faça backup automático do arquivo de dados antes de operações críticas

5. **Extras** (opcional):
   - Adicione prioridades às tarefas
   - Implemente lembretes para tarefas próximas do prazo
   - Adicione categorias ou tags às tarefas
   - Crie uma interface web usando Flask ou FastAPI

## Dicas para os Exercícios

1. Sempre feche os arquivos após o uso (use `with`)
2. Use codificação UTF-8 ao trabalhar com texto
3. Valide sempre se os arquivos/diretórios existem antes de tentar acessá-los
4. Use expressões regulares para validação e extração de padrões
5. Escreva funções pequenas e com responsabilidade única
6. Documente seu código com docstrings e comentários quando necessário
7. Escreva testes para suas funções

## Exemplo de Solução para o Exercício 1

```python
import re
from collections import defaultdict

def contar_palavras(caminho_arquivo):
    """
    Conta a ocorrência de cada palavra em um arquivo de texto.
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo de texto
        
    Returns:
        dict: Dicionário com as palavras e suas contagens
    """
    contagem = defaultdict(int)
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Remove pontuação e divide em palavras
                palavras = re.findall(r'\b\w+\b', linha.lower())
                for palavra in palavras:
                    contagem[palavra] += 1
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {caminho_arquivo}")
        return {}
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return {}
    
    return dict(contagem)

# Exemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Uso: python contador.py <arquivo>")
        sys.exit(1)
    
    resultado = contar_palavras(sys.argv[1])
    for palavra, quantidade in sorted(resultado.items(), key=lambda x: x[1], reverse=True):
        print(f"{palavra}: {quantidade}")
```

## Recursos Adicionais

1. [Documentação do Python - Leitura e Escrita de Arquivos](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
2. [Documentação do módulo `csv`](https://docs.python.org/3/library/csv.html)
3. [Expressões Regulares em Python](https://docs.python.org/3/howto/regex.html)
4. [Trabalhando com arquivos e diretórios](https://docs.python.org/3/library/os.path.html)
5. [Tutorial de manipulação de caminhos com `pathlib`](https://docs.python.org/3/library/pathlib.html)
