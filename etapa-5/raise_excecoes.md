# Levantando Exceções com `raise` em Python

Além de capturar exceções, você pode querer levantá-las explicitamente em seu código para sinalizar erros ou condições excepcionais. O comando `raise` é usado para esse propósito.

## Sintaxe Básica

A forma mais simples de levantar uma exceção é usando o comando `raise` seguido de uma instância de exceção:

```python
raise Exception("Algo deu errado!")
```

## Tipos de Exceções

Python possui várias exceções embutidas que você pode usar:

```python
# Erro de valor
raise ValueError("Valor inválido")

# Erro de tipo
raise TypeError("Tipo de dado inválido")

# Erro de chave
raise KeyError("Chave não encontrada")

# Erro de índice
raise IndexError("Índice fora do intervalo")

# Erro de atributo
raise AttributeError("Atributo não encontrado")
```

## Criando Exceções Personalizadas

Você pode criar suas próprias exceções herdando da classe base `Exception`:

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
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
    print(f"Saldo atual: R${e.saldo_atual:.2f}")
    print(f"Valor tentado de saque: R${e.valor_saque:.2f}")
```

## Relançando Exceções

Às vezes, você pode querer capturar uma exceção, fazer algum tratamento e depois relançá-la:

```python
def processar_arquivo(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        raise  # Relança a exceção capturada

try:
    conteudo = processar_arquivo("arquivo_inexistente.txt")
except FileNotFoundError:
    print("Não foi possível processar o arquivo.")
```

## Encadeamento de Exceções

Python 3 permite encadear exceções para rastrear a causa raiz de um problema:

```python
def processar_dados(dados):
    try:
        return int(dados)
    except ValueError as e:
        # Cria uma nova exceção com a original como causa
        raise RuntimeError("Falha ao processar os dados") from e

try:
    resultado = processar_dados("abc")
except RuntimeError as e:
    print(f"Erro: {e}")
    print(f"Causa: {e.__cause__}")
```

## Levantando Exceções com Informações Adicionais

Você pode adicionar atributos personalizados às suas exceções para fornecer mais contexto:

```python
class ErroValidacao(Exception):
    """Exceção base para erros de validação."""
    def __init__(self, mensagem, campo=None, valor=None):
        self.mensagem = mensagem
        self.campo = campo
        self.valor = valor
        super().__init__(mensagem)

def validar_idade(idade):
    if not isinstance(idade, int):
        raise ErroValidacao("Idade deve ser um número", "idade", idade)
    if idade < 0:
        raise ErroValidacao("Idade não pode ser negativa", "idade", idade)
    if idade > 120:
        raise ErroValidacao("Idade inválida", "idade", idade)
    return True

try:
    validar_idade(-5)
except ErroValidacao as e:
    print(f"Erro de validação no campo '{e.campo}': {e.mensagem}")
    print(f"Valor inválido: {e.valor}")
```

## Boas Práticas

1. **Seja específico**: Use o tipo de exceção mais específico possível.
2. **Documente as exceções**: Use docstrings para documentar quais exceções uma função pode levantar.
3. **Forneça mensagens úteis**: Inclua informações relevantes na mensagem de erro.
4. **Não abuse de exceções**: Use exceções apenas para situações excepcionais, não para controle de fluxo normal.
5. **Mantenha a hierarquia de exceções**: Crie hierarquias lógicas de exceções personalizadas.

## Exemplo Completo

```python
class ErroAutenticacao(Exception):
    """Exceção base para erros de autenticação."""
    pass

class UsuarioNaoEncontradoError(ErroAutenticacao):
    """Exceção lançada quando o usuário não é encontrado."""
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f"Usuário não encontrado: {usuario}")

class SenhaIncorretaError(ErroAutenticacao):
    """Exceção lançada quando a senha está incorreta."""
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f"Senha incorreta para o usuário: {usuario}")

class ContaBloqueadaError(ErroAutenticacao):
    """Exceção lançada quando a conta está bloqueada."""
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(f"Conta bloqueada para o usuário: {usuario}")

def autenticar(usuario, senha):
    """
    Autentica um usuário com nome de usuário e senha.
    
    Args:
        usuario: Nome de usuário
        senha: Senha do usuário
        
    Returns:
        bool: True se a autenticação for bem-sucedida
        
    Raises:
        UsuarioNaoEncontradoError: Se o usuário não existir
        SenhaIncorretaError: Se a senha estiver incorreta
        ContaBloqueadaError: Se a conta estiver bloqueada
    """
    # Simulando uma base de dados de usuários
    usuarios = {
        "admin": {"senha": "admin123", "bloqueado": False},
        "usuario1": {"senha": "senha123", "bloqueado": False},
        "bloqueado": {"senha": "senha123", "bloqueado": True}
    }
    
    if usuario not in usuarios:
        raise UsuarioNaoEncontradoError(usuario)
        
    if usuarios[usuario]["bloqueado"]:
        raise ContaBloqueadaError(usuario)
        
    if usuarios[usuario]["senha"] != senha:
        raise SenhaIncorretaError(usuario)
        
    return True

def main():
    """Função principal para demonstrar o tratamento de exceções."""
    tentativas = [
        ("usuario_inexistente", "senha"),
        ("admin", "senha_errada"),
        ("bloqueado", "senha123"),
        ("admin", "admin123")
    ]
    
    for usuario, senha in tentativas:
        try:
            print(f"\nTentando autenticar: {usuario}")
            autenticar(usuario, senha)
            print("Autenticação bem-sucedida!")
            
        except UsuarioNaoEncontradoError as e:
            print(f"Erro: {e}")
            print("Por favor, verifique o nome de usuário.")
            
        except SenhaIncorretaError as e:
            print(f"Erro: {e}")
            print("Por favor, verifique sua senha.")
            
        except ContaBloqueadaError as e:
            print(f"Erro: {e}")
            print("Entre em contato com o suporte para desbloquear sua conta.")
            
        except ErroAutenticacao as e:
            print(f"Erro de autenticação: {e}")
            
        except Exception as e:
            print(f"Erro inesperado: {e}")
            
        else:
            print("Acesso concedido!")
            
        finally:
            print("Tentativa de login finalizada.")

if __name__ == "__main__":
    main()
```

## Exercícios

1. **Validador de Formulário**: Crie uma função que valide um formulário com nome, e-mail e senha, levantando exceções personalizadas para cada tipo de erro de validação.

2. **Calculadora Científica**: Implemente uma calculadora que aceite operações avançadas (raiz quadrada, logaritmo, etc.) e levante exceções apropriadas para entradas inválidas.

3. **Sistema de Arquivos**: Crie uma classe para gerenciar operações de arquivos (criar, ler, atualizar, excluir) com tratamento adequado de exceções.

4. **API REST**: Implemente um cliente para uma API REST que lide adequadamente com diferentes códigos de status HTTP, convertendo-os em exceções apropriadas.

5. **Jogo de Xadrez**: Desenvolva um jogo de xadrez onde movimentos inválidos levantem exceções específicas (ex: `MovimentoInvalidoError`, `ReiEmXequeError`, etc.).
