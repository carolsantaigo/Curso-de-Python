# Tratamento de Exceções em Python

O tratamento de exceções em Python permite que você lide com erros de forma elegante e evite que seu programa quebre inesperadamente. Este guia cobre o uso de `try`, `except`, `else` e `finally` para gerenciar exceções.

## O Básico: try/except

A estrutura básica de tratamento de exceções em Python é composta por blocos `try` e `except`.

### Sintaxe Básica

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ocorrer
    print("Erro: Divisão por zero não é permitida.")
```

### Capturando Múltiplas Exceções

Você pode capturar diferentes tipos de exceções em um único bloco `try`:

```python
try:
    # Código que pode gerar várias exceções
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except ValueError:
    print("Erro: Por favor, digite um número válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
```

### Capturando Todas as Exceções (Não Recomendado)

Embora possível, capturar todas as exceções sem especificar o tipo geralmente não é uma boa prática, pois pode mascarar erros inesperados.

```python
try:
    # Código perigoso
    resultado = 10 / 0
except:  # Captura qualquer exceção (evite usar assim)
    print("Ocorreu um erro inesperado!")
```

### Capturando a Instância da Exceção

Você pode capturar a instância da exceção para obter mais informações:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")  # Exibe a mensagem de erro
    print(f"Tipo do erro: {type(e).__name__}")
```

## O Bloco else

O bloco `else` é executado apenas se nenhuma exceção for lançada no bloco `try`.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Erro: {e}")
else:
    print(f"Operação bem-sucedida! Resultado: {resultado}")
```

## O Bloco finally

O bloco `finally` é sempre executado, independentemente de uma exceção ter ocorrido ou não. É útil para ações de limpeza.

```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    numero = int(conteudo)
    print(f"O número é {numero}")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except ValueError:
    print("O arquivo não contém um número válido.")
finally:
    # Garante que o arquivo será fechado, mesmo que ocorra uma exceção
    if 'arquivo' in locals() and not arquivo.closed:
        arquivo.close()
    print("Operação finalizada.")
```

## Gerenciadores de Contexto (with)

Uma forma mais limpa de lidar com recursos que precisam ser limpos é usar a instrução `with`:

```python
try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        numero = int(conteudo)
        print(f"O número é {numero}")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except ValueError:
    print("O arquivo não contém um número válido.")
# Não é necessário fechar o arquivo manualmente
```

## Encadeamento de Exceções

Python 3 permite encadear exceções para rastrear a causa raiz de um erro:

```python
try:
    # Código que pode falhar
    with open("arquivo_inexistente.txt") as f:
        conteudo = f.read()
except FileNotFoundError as e:
    # Lança uma nova exceção com a original como causa
    raise RuntimeError("Falha ao processar o arquivo") from e
```

## Exceções Personalizadas

Você pode criar suas próprias exceções para representar erros específicos da sua aplicação:

```python
class SaldoInsuficienteError(Exception):
    """Exceção lançada quando não há saldo suficiente para uma operação."""
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        mensagem = f"Saldo insuficiente: R${saldo_atual:.2f} para sacar R${valor_saque:.2f}"
        super().__init__(mensagem)

def sacar(saldo_atual, valor_saque):
    if valor_saque > saldo_atual:
        raise SaldoInsuficienteError(saldo_atual, valor_saque)
    return saldo_atual - valor_saque

try:
    saldo = 100.0
    saque = 150.0
    novo_saldo = sacar(saldo, saque)
    print(f"Saque realizado. Novo saldo: R${novo_saldo:.2f}")
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
```

## Boas Práticas

1. **Seja específico nas exceções**: Capture apenas as exceções que você espera e sabe como tratar.
2. **Documente as exceções**: Use docstrings para documentar quais exceções uma função pode lançar.
3. **Não use exceções para fluxo de controle**: Exceções são para situações excepcionais, não para controle de fluxo normal.
4. **Limpe os recursos**: Use `finally` ou gerenciadores de contexto para garantir que os recursos sejam liberados.
5. **Registre os erros**: Em aplicações reais, registre os erros em um arquivo de log para análise posterior.

## Exemplo Completo

```python
import logging
from typing import Union, Optional

# Configuração básica de logging
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def dividir_numeros() -> Optional[float]:
    """
    Divide 10 por um número fornecido pelo usuário.
    
    Returns:
        float: O resultado da divisão, ou None em caso de erro.
        
    Raises:
        ValueError: Se o valor digitado não for um número.
        ZeroDivisionError: Se o número digitado for zero.
    """
    try:
        # Tenta converter a entrada para float
        numero = float(input("Digite um número para dividir 10: "))
        
        # Verifica se o número é zero
        if numero == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
            
        resultado = 10 / numero
        
    except ValueError as ve:
        # Captura erros de conversão de tipo
        logging.error(f"Valor inválido: {ve}")
        print("Erro: Por favor, digite um número válido.")
        return None
        
    except ZeroDivisionError as zde:
        # Captura divisão por zero
        logging.error(f"Tentativa de divisão por zero: {zde}")
        print("Erro: Não é possível dividir por zero.")
        return None
        
    except Exception as e:
        # Captura qualquer outra exceção inesperada
        logging.error(f"Erro inesperado: {e}", exc_info=True)
        print("Ocorreu um erro inesperado. Por favor, tente novamente.")
        return None
        
    else:
        # Executa apenas se não houve exceções
        print("Operação realizada com sucesso!")
        return resultado
        
    finally:
        # Sempre executa, com ou sem exceções
        print("Fim da operação de divisão.")

# Exemplo de uso
if __name__ == "__main__":
    resultado = dividir_numeros()
    if resultado is not None:
        print(f"O resultado é: {resultado:.2f}")
```

## Exercícios

1. **Validador de E-mail**: Escreva uma função que valide um endereço de e-mail. A função deve lançar exceções personalizadas para diferentes tipos de erros (formato inválido, domínio inexistente, etc.).

2. **Calculadora com Tratamento de Erros**: Crie uma calculadora que aceite operações básicas (+, -, *, /) e trate adequadamente os erros que podem ocorrer.

3. **Gerenciador de Arquivos**: Implemente um gerenciador de arquivos que permita ler, escrever e apagar arquivos, com tratamento adequado para erros de permissão, arquivo não encontrado, etc.

4. **API de Clima**: Escreva uma função que faça uma requisição a uma API de previsão do tempo e trate os possíveis erros de rede, formato de dados inesperado, etc.

5. **Banco de Dados**: Crie uma classe para gerenciar conexões com um banco de dados SQLite, com tratamento adequado para erros de conexão, consultas inválidas, etc.
