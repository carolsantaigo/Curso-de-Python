# Projeto Prático: Leitor de Arquivos e Extrator de Informações

Neste projeto, você criará um programa em Python que lê arquivos de texto, extrai informações específicas e gera relatórios. O programa será capaz de processar diferentes tipos de arquivos e extrair estatísticas úteis.

## Objetivos

1. Ler e processar arquivos de texto e CSV
2. Extrair informações específicas dos arquivos
3. Gerar relatórios formatados
4. Implementar tratamento de erros
5. Criar uma interface de linha de comando amigável

## Requisitos

- Python 3.6+
- Módulos padrão: `os`, `csv`, `re`, `argparse`, `collections`
- Opcional: `pandas` para processamento avançado de dados

## Estrutura do Projeto

```
leitor_arquivos/
├── README.md
├── requirements.txt
├── leitor_arquivos/
│   ├── __init__.py
│   ├── __main__.py
│   ├── processadores.py
│   ├── relatorios.py
│   └── utils.py
└── exemplos/
    ├── dados.csv
    └── log.txt
```

## Implementação

### 1. Estrutura Básica

Primeiro, vamos criar a estrutura básica do projeto:

```bash
mkdir -p leitor_arquivos/leitor_arquivos leitor_arquivos/exemplos
cd leitor_arquivos
```

### 2. requirements.txt

```
pandas>=1.3.0
```

### 3. leitor_arquivos/__init__.py

```python
"""Pacote Leitor de Arquivos - Extraia informações de arquivos de texto e CSV."""

__version__ = '0.1.0'
```

### 4. leitor_arquivos/utils.py

```python
import os
import re
from typing import List, Dict, Any, Union, Optional

def validar_arquivo(caminho: str) -> bool:
    """Verifica se o arquivo existe e é acessível."""
    return os.path.isfile(caminho) and os.access(caminho, os.R_OK)

def extrair_emails(texto: str) -> List[str]:
    """Extrai endereços de email de um texto."""
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(padrao, texto)

def extrair_telefones(texto: str) -> List[str]:
    """Extrai números de telefone de um texto."""
    # Padrão para telefones brasileiros: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX
    padrao = r'\(\d{2}\)\s\d{4,5}-\d{4}'
    return re.findall(padrao, texto)

def formatar_tamanho(tamanho_bytes: int) -> str:
    """Formata o tamanho do arquivo em uma string legível."""
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if tamanho_bytes < 1024.0:
            return f"{tamanho_bytes:.2f} {unidade}"
        tamanho_bytes /= 1024.0
    return f"{tamanho_bytes:.2f} TB"
```

### 5. leitor_arquivos/processadores.py

```python
import csv
import os
from typing import Dict, List, Any, Optional
from collections import defaultdict

from . import utils

class ProcessadorTexto:
    """Processa arquivos de texto e extrai informações."""
    
    def __init__(self, caminho_arquivo: str):
        self.caminho = caminho_arquivo
        self.estatisticas: Dict[str, Any] = {
            'linhas': 0,
            'palavras': 0,
            'caracteres': 0,
            'emails': [],
            'telefones': [],
            'palavras_contagem': defaultdict(int),
            'tamanho_arquivo': 0
        }
    
    def processar(self) -> Dict[str, Any]:
        """Processa o arquivo de texto e retorna estatísticas."""
        if not utils.validar_arquivo(self.caminho):
            raise FileNotFoundError(f"Arquivo não encontrado ou sem permissão: {self.caminho}")
        
        self.estatisticas['tamanho_arquivo'] = os.path.getsize(self.caminho)
        
        with open(self.caminho, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                self.estatisticas['linhas'] += 1
                self.estatisticas['caracteres'] += len(linha)
                
                # Processa palavras
                palavras = linha.strip().split()
                self.estatisticas['palavras'] += len(palavras)
                
                for palavra in palavras:
                    palavra = palavra.lower().strip('.,!?;:')
                    if palavra:
                        self.estatisticas['palavras_contagem'][palavra] += 1
                
                # Extrai emails e telefones
                self.estatisticas['emails'].extend(utils.extrair_emails(linha))
                self.estatisticas['telefones'].extend(utils.extrair_telefones(linha))
        
        # Remove duplicatas
        self.estatisticas['emails'] = list(set(self.estatisticas['emails']))
        self.estatisticas['telefones'] = list(set(self.estatisticas['telefones']))
        
        return self.estatisticas


class ProcessadorCSV:
    """Processa arquivos CSV e extrai informações."""
    
    def __init__(self, caminho_arquivo: str, delimitador: str = ','):
        self.caminho = caminho_arquivo
        self.delimitador = delimitador
        self.dados: List[Dict[str, Any]] = []
        self.colunas: List[str] = []
    
    def processar(self) -> Dict[str, Any]:
        """Processa o arquivo CSV e retorna estatísticas."""
        if not utils.validar_arquivo(self.caminho):
            raise FileNotFoundError(f"Arquivo não encontrado ou sem permissão: {self.caminho}")
        
        with open(self.caminho, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=self.delimitador)
            self.colunas = leitor.fieldnames or []
            self.dados = list(leitor)
        
        return self.gerar_relatorio()
    
    def gerar_relatorio(self) -> Dict[str, Any]:
        """Gera um relatório com estatísticas do CSV."""
        if not self.dados:
            return {}
        
        relatorio = {
            'total_linhas': len(self.dados),
            'colunas': self.colunas,
            'tipos_dados': {},
            'valores_unicos': {},
            'valores_nulos': {}
        }
        
        for coluna in self.colunas:
            valores = [str(linha.get(coluna, '')).strip() for linha in self.dados]
            relatorio['valores_unicos'][coluna] = len(set(valores))
            relatorio['valores_nulos'][coluna] = sum(1 for v in valores if not v)
            
            # Tenta inferir o tipo de dados
            tipos = set()
            for valor in valores:
                if not valor:
                    continue
                try:
                    int(valor)
                    tipos.add('inteiro')
                except ValueError:
                    try:
                        float(valor)
                        tipos.add('decimal')
                    except ValueError:
                        tipos.add('texto')
            
            relatorio['tipos_dados'][coluna] = sorted(list(tipos)) if tipos else ['desconhecido']
        
        return relatorio
```

### 6. leitor_arquivos/relatorios.py

```python
from typing import Dict, Any
import json

from . import utils

def gerar_relatorio_texto(estatisticas: Dict[str, Any]) -> str:
    """Gera um relatório formatado para arquivos de texto."""
    relatorio = [
        "=== Relatório de Análise de Texto ===\n",
        f"Arquivo analisado: {estatisticas.get('caminho', 'N/A')}",
        f"Tamanho do arquivo: {utils.formatar_tamanho(estatisticas.get('tamanho_arquivo', 0))}",
        f"Total de linhas: {estatisticas.get('linhas', 0):,}",
        f"Total de palavras: {estatisticas.get('palavras', 0):,}",
        f"Total de caracteres: {estatisticas.get('caracteres', 0):,}\n",
        "=== Informações de Contato ===",
        f"E-mails encontrados: {len(estatisticas.get('emails', []))}",
        "\n".join(f"  - {email}" for email in estatisticas.get('emails', [])),
        f"\nTelefones encontrados: {len(estatisticas.get('telefones', []))}",
        "\n".join(f"  - {tel}" for tel in estatisticas.get('telefones', [])),
        "\n\n=== Palavras mais frequentes ==="
    ]
    
    # Adiciona as 10 palavras mais frequentes
    palavras = estatisticas.get('palavras_contagem', {})
    if palavras:
        mais_frequentes = sorted(
            palavras.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]
        
        for palavra, contagem in mais_frequentes:
            relatorio.append(f"{palavra}: {contagem} ocorrências")
    
    return "\n".join(relatorio)

def gerar_relatorio_csv(estatisticas: Dict[str, Any]) -> str:
    """Gera um relatório formatado para arquivos CSV."""
    relatorio = [
        "=== Relatório de Análise CSV ===\n",
        f"Arquivo analisado: {estatisticas.get('caminho', 'N/A')}",
        f"Total de linhas: {estatisticas.get('total_linhas', 0):,}",
        f"Colunas: {', '.join(estatisticas.get('colunas', []))}\n",
        "=== Estatísticas por Coluna ===\n"
    ]
    
    for coluna in estatisticas.get('colunas', []):
        relatorio.extend([
            f"Coluna: {coluna}",
            f"  Tipo de dados: {', '.join(estatisticas.get('tipos_dados', {}).get(coluna, ['desconhecido']))}",
            f"  Valores únicos: {estatisticas.get('valores_unicos', {}).get(coluna, 0):,}",
            f"  Valores nulos: {estatisticas.get('valores_nulos', {}).get(coluna, 0):,}\n"
        ])
    
    return "\n".join(relatorio)

def salvar_relatorio(conteudo: str, caminho_saida: str) -> None:
    """Salva o relatório em um arquivo."""
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
```

### 7. leitor_arquivos/__main__.py

```python
#!/usr/bin/env python3
"""Leitor de Arquivos - Ferramenta de análise de arquivos de texto e CSV."""

import argparse
import os
import sys
from pathlib import Path

from .processadores import ProcessadorTexto, ProcessadorCSV
from .relatorios import gerar_relatorio_texto, gerar_relatorio_csv, salvar_relatorio

def parse_args():
    """Configura os argumentos de linha de comando."""
    parser = argparse.ArgumentParser(
        description='Analisa arquivos de texto e CSV, extraindo informações úteis.'
    )
    
    parser.add_argument(
        'arquivo',
        type=str,
        help='Caminho para o arquivo a ser analisado'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Arquivo de saída para o relatório (opcional)',
        default=None
    )
    
    parser.add_argument(
        '--delimitador',
        type=str,
        default=',',
        help='Delimitador para arquivos CSV (padrão: ,)'
    )
    
    return parser.parse_args()

def main():
    """Função principal."""
    args = parse_args()
    
    try:
        # Verifica se o arquivo existe
        if not os.path.isfile(args.arquivo):
            print(f"Erro: Arquivo não encontrado: {args.arquivo}", file=sys.stderr)
            sys.exit(1)
        
        # Determina o tipo de processador com base na extensão
        extensao = Path(args.arquivo).suffix.lower()
        
        if extensao == '.csv':
            processador = ProcessadorCSV(args.arquivo, args.delimitador)
            estatisticas = processador.processar()
            relatorio = gerar_relatorio_csv(estatisticas)
        else:
            # Assume que é um arquivo de texto
            processador = ProcessadorTexto(args.arquivo)
            estatisticas = processador.processar()
            relatorio = gerar_relatorio_texto(estatisticas)
        
        # Adiciona o caminho do arquivo ao relatório
        estatisticas['caminho'] = os.path.abspath(args.arquivo)
        
        # Exibe ou salva o relatório
        if args.output:
            salvar_relatorio(relatorio, args.output)
            print(f"Relatório salvo em: {os.path.abspath(args.output)}")
        else:
            print(relatorio)
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## Como Usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o leitor de arquivos:
   ```bash
   # Para um arquivo de texto
   python -m leitor_arquivos caminho/para/arquivo.txt
   
   # Para um arquivo CSV
   python -m leitor_arquivos caminho/para/dados.csv
   
   # Para salvar o relatório em um arquivo
   python -m leitor_arquivos caminho/para/arquivo.txt -o relatorio.txt
   
   # Especificar delimitador para CSV
   python -m leitor_arquivos dados.csv --delimitador ';' -o relatorio.csv
   ```

## Exemplos de Saída

### Para arquivos de texto:
```
=== Relatório de Análise de Texto ===

Arquivo analisado: /caminho/para/arquivo.txt
Tamanho do arquivo: 1.23 MB
Total de linhas: 1,234
Total de palavras: 9,876
Total de caracteres: 56,789

=== Informações de Contato ===
E-mails encontrados: 2
  - contato@exemplo.com
  - suporte@empresa.com.br

Telefones encontrados: 1
  - (11) 98765-4321

=== Palavras mais frequentes ===
python: 45 ocorrências
dados: 32 ocorrências
arquivo: 28 ocorrências
```

### Para arquivos CSV:
```
=== Relatório de Análise CSV ===

Arquivo analisado: /caminho/para/dados.csv
Total de linhas: 1,000
Colunas: id, nome, email, telefone, cidade

=== Estatísticas por Coluna ===

Coluna: id
  Tipo de dados: inteiro
  Valores únicos: 1,000
  Valores nulos: 0

Coluna: nome
  Tipo de dados: texto
  Valores únicos: 987
  Valores nulos: 2
```

## Exercícios de Melhoria

1. Adicione suporte a mais formatos de arquivo (JSON, Excel, etc.)
2. Implemente análise de sentimento para arquivos de texto
3. Adicione opção para filtrar dados antes de gerar o relatório
4. Crie visualizações gráficas usando matplotlib ou outra biblioteca
5. Adicione suporte a processamento em lote de múltiplos arquivos
6. Implemente um servidor web para usar a ferramenta via navegador
