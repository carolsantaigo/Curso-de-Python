# Boas Práticas para Mensagens de Erro em Python

Mensagens de erro claras e informativas são essenciais para uma boa experiência de desenvolvimento e depuração. Este guia apresenta as melhores práticas para criar mensagens de erro úteis em Python.

## 1. Seja Claro e Específico

### Ruim:
```python
raise ValueError("Valor inválido")
```

### Bom:
```python
raise ValueError("O valor da idade deve ser um número inteiro entre 0 e 120")
```

## 2. Inclua o Valor Problemático

### Ruim:
```python
if not isinstance(idade, int):
    raise TypeError("Tipo de dado inválido")
```

### Bom:
```python
if not isinstance(idade, int):
    raise TypeError(f"A idade deve ser um número inteiro, mas recebeu {idade} (tipo: {type(idade).__name__})")
```

## 3. Use a Estrutura "O que aconteceu" + "Por quê" + "Como corrigir"

### Exemplo:
```python
def calcular_media(numeros):
    if not numeros:
        raise ValueError(
            "Não foi possível calcular a média. "  # O que aconteceu
            "A lista de números está vazia. "      # Por quê
            "Forneça uma lista com pelo menos um número."  # Como corrigir
        )
    return sum(numeros) / len(numeros)
```

## 4. Use Exceções Personalizadas para Casos Específicos

```python
class ErroValidacaoDados(Exception):
    """Exceção base para erros de validação de dados."""
    pass

class EmailInvalidoError(ErroValidacaoDados):
    """Exceção lançada quando um e-mail é inválido."""
    def __init__(self, email):
        self.email = email
        super().__init__(f"O e-mail '{email}' não é válido. Certifique-se de que contém um @ e um domínio válido.")

def validar_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise EmailInvalidoError(email)
    return True
```

## 5. Adicione Contexto às Exceções

Use `raise ... from` para encadear exceções e fornecer contexto adicional:

```python
def processar_arquivo(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return arquivo.read()
    except IOError as e:
        raise RuntimeError(f"Falha ao processar o arquivo {caminho}") from e
```

## 6. Documente as Exceções

Use docstrings para documentar quais exceções uma função pode levantar:

```python
def dividir(a, b):
    """
    Divide dois números.
    
    Args:
        a: Numerador
        b: Denominador
        
    Returns:
        float: O resultado da divisão a / b
        
    Raises:
        ValueError: Se b for zero
        TypeError: Se a ou b não forem números
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos os argumentos devem ser números")
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b
```

## 7. Use Constantes para Mensagens de Erro Recorrentes

```python
class MensagensErro:
    VALOR_NEGATIVO = "O valor não pode ser negativo: {valor}"
    TIPO_INVALIDO = "Tipo inválido. Esperado: {esperado}, Obtido: {obtido}"
    
def validar_idade(idade):
    if not isinstance(idade, int):
        raise TypeError(MensagensErro.TIPO_INVALIDO.format(
            esperado="int",
            obtido=type(idade).__name__
        ))
    if idade < 0:
        raise ValueError(MensagensErro.VALOR_NEGATIVO.format(valor=idade))
    return idade
```

## 8. Forneça Informações de Recuperação

Inclua sugestões sobre como corrigir o erro:

```python
def configurar_banco_dados(config):
    if 'host' not in config:
        raise ValueError(
            "Configuração de banco de dados incompleta. "
            "O arquivo de configuração deve incluir 'host'.\n"
            "Exemplo de configuração válida:\n"
            "config = {\n                'host': 'localhost',\n                'port': 5432,\n                'database': 'meu_banco'\n            }"
        )
```

## 9. Use o Módulo `logging` para Registrar Erros

```python
import logging

def processar_dados(dados):
    logger = logging.getLogger(__name__)
    
    try:
        # Código que pode falhar
        resultado = int(dados)
        return resultado
        
    except ValueError as e:
        # Log detalhado para desenvolvedores
        logger.error(
            "Falha ao converter dados para inteiro",
            exc_info=True,
            extra={"dados_recebidos": dados, "tipo_dados": type(dados).__name__}
        )
        # Mensagem amigável para o usuário
        raise ValueError("Os dados fornecidos não são um número válido") from e
```

## 10. Teste Suas Mensagens de Erro

Certifique-se de que suas mensagens de erro são úteis testando-as:

```python
import unittest

class TestValidacaoEmail(unittest.TestCase):
    def test_email_invalido(self):
        with self.assertRaises(EmailInvalidoError) as context:
            validar_email("email_invalido")
            
        self.assertIn("não é válido", str(context.exception))
        self.assertIn("@", str(context.exception))
```

## Exemplo Completo: Validador de Usuário

```python
class ErroValidacaoUsuario(Exception):
    """Exceção base para erros de validação de usuário."""
    pass

class NomeUsuarioInvalidoError(ErroValidacaoUsuario):
    """Exceção lançada quando o nome de usuário é inválido."""
    def __init__(self, nome, motivo):
        self.nome = nome
        self.motivo = motivo
        super().__init__(f"Nome de usuário inválido: {motivo}")

class SenhaFracaError(ErroValidacaoUsuario):
    """Exceção lançada quando a senha não atende aos requisitos."""
    def __init__(self, requisitos_nao_atendidos):
        self.requisitos_nao_atendidos = requisitos_nao_atendidos
        mensagem = "A senha não atende aos seguintes requisitos:\n"
        mensagem += "\n".join(f"- {req}" for req in requisitos_nao_atendidos)
        super().__init__(mensagem)

def validar_nome_usuario(nome):
    """
    Valida um nome de usuário.
    
    Args:
        nome: Nome de usuário a ser validado
        
    Raises:
        NomeUsuarioInvalidoError: Se o nome de usuário for inválido
    """
    if not nome:
        raise NomeUsuarioInvalidoError(nome, "não pode estar vazio")
    if len(nome) < 3:
        raise NomeUsuarioInvalidoError(nome, "deve ter pelo menos 3 caracteres")
    if len(nome) > 20:
        raise NomeUsuarioInvalidoError(nome, "não pode ter mais de 20 caracteres")
    if not nome.isalnum():
        raise NomeUsuarioInvalidoError(
            nome, 
            "deve conter apenas letras e números"
        )
    return True

def validar_senha(senha):
    """
    Valida uma senha.
    
    Args:
        senha: Senha a ser validada
        
    Raises:
        SenhaFracaError: Se a senha não atender aos requisitos
    """
    requisitos_nao_atendidos = []
    
    if len(senha) < 8:
        requisitos_nao_atendidos.append("Pelo menos 8 caracteres")
    if not any(c.isupper() for c in senha):
        requisitos_nao_atendidos.append("Pelo menos uma letra maiúscula")
    if not any(c.islower() for c in senha):
        requisitos_nao_atendidos.append("Pelo menos uma letra minúscula")
    if not any(c.isdigit() for c in senha):
        requisitos_nao_atendidos.append("Pelo menos um número")
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in senha):
        requisitos_nao_atendidos.append("Pelo menos um caractere especial")
    
    if requisitos_nao_atendidos:
        raise SenhaFracaError(requisitos_nao_atendidos)
    
    return True

def criar_usuario(nome, senha):
    """
    Cria um novo usuário.
    
    Args:
        nome: Nome de usuário
        senha: Senha do usuário
        
    Returns:
        dict: Dados do usuário criado
        
    Raises:
        NomeUsuarioInvalidoError: Se o nome de usuário for inválido
        SenhaFracaError: Se a senha não atender aos requisitos
    """
    validar_nome_usuario(nome)
    validar_senha(senha)
    
    # Se chegou aqui, os dados são válidos
    return {"nome": nome, "senha": "*" * len(senha)}

# Exemplo de uso
try:
    usuario = criar_usuario("usuario1", "Senha123!")
    print(f"Usuário criado com sucesso: {usuario['nome']}")
    
except NomeUsuarioInvalidoError as e:
    print(f"Erro no nome de usuário: {e}")
    
except SenhaFracaError as e:
    print(f"Senha fraca: {e}")
    
except ErroValidacaoUsuario as e:
    print(f"Erro de validação: {e}")
    
except Exception as e:
    print(f"Erro inesperado: {e}")
```

## Exercícios

1. **Validador de Endereço de E-mail**: Melhore a função de validação de e-mail para fornecer mensagens de erro mais específicas (ex.: domínio inválido, sem @, etc.).

2. **Validador de CPF**: Crie uma função que valide CPFs, com mensagens de erro específicas para cada tipo de problema (tamanho, dígitos inválidos, etc.).

3. **API de Pagamento**: Implemente uma classe para processar pagamentos com tratamento de erros detalhado para diferentes cenários (cartão expirado, saldo insuficiente, etc.).

4. **Conversor de Temperatura**: Crie uma função que converta entre Celsius, Fahrenheit e Kelvin, com tratamento de erros para valores abaixo do zero absoluto.

5. **Gerenciador de Tarefas**: Desenvolva um sistema de gerenciamento de tarefas com validação de datas e prioridades, com mensagens de erro claras para conflitos de agendamento.
