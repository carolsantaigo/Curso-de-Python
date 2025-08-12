# Exercícios - Tratamento de Erros e Debug

## Exercícios Básicos

### 1. Validador de E-mail
Escreva uma função que valide endereços de e-mail, levantando exceções personalizadas para diferentes tipos de erros:
- Formato inválido (falta de @ ou domínio)
- Nome de usuário inválido (caracteres não permitidos)
- Domínio inválido (sem ponto, muito curto, etc.)

### 2. Calculadora com Tratamento de Erros
Crie uma calculadora que aceite operações básicas (+, -, *, /) e trate os seguintes erros:
- Divisão por zero
- Entrada não numérica
- Operador inválido

### 3. Gerenciador de Arquivos
Implemente funções para ler, escrever e apagar arquivos com tratamento adequado para:
- Arquivo não encontrado
- Permissão negada
- Disco cheio
- Erros de E/S

## Exercícios Intermediários

### 4. Validador de CPF
Crie uma função que valide números de CPF, verificando:
- Formato (apenas dígitos, 11 caracteres)
- Dígitos verificadores
- CPFs inválidos conhecidos (todos dígitos iguais)

### 5. API de Clima
Escreva uma função que consulte uma API de previsão do tempo e trate:
- Erros de conexão
- Respostas inesperadas da API
- Dados ausentes
- Limites de taxa de requisição

### 6. Conversor de Moedas
Implemente um conversor de moedas que:
- Valide os códigos de moeda
- Trate erros de conexão com a API de cotações
- Lide com valores monetários inválidos
- Mantenha um cache local para funcionar offline

## Exercícios Avançados

### 7. Sistema de Banco de Dados
Crie uma classe para gerenciar um banco de dados SQLite com tratamento de:
- Conexões vazando
- Transações falhas
- Concorrência
- Rollback em caso de erro

### 8. Web Scraper Resiliente
Desenvolva um web scraper que:
- Lide com falhas de rede
- Respeite os limites do servidor (robots.txt)
- Gerencie sessões e cookies
- Trate mudanças na estrutura da página

### 9. Processador de Dados em Lote
Implemente um sistema que processe arquivos CSV grandes com tratamento para:
- Arquivos corrompidos
- Dados ausentes ou inválidos
- Interrupções durante o processamento
- Retomada de processamento interrompido

## Projeto Final: Sistema de Gerenciamento de Tarefas

Desenvolva um aplicativo de linha de comando para gerenciar tarefas com tratamento robusto de erros:

### Requisitos:

1. **Armazenamento**:
   - Use SQLite para armazenar as tarefas
   - Implemente backup automático dos dados
   - Trate erros de concorrência

2. **Funcionalidades**:
   - Adicionar tarefa com descrição e prazo
   - Listar tarefas (todas, por status, por data)
   - Marcar tarefa como concluída
   - Remover tarefa
   - Buscar tarefas por palavra-chave
   - Exportar/importar tarefas para JSON

3. **Tratamento de Erros**:
   - Valide todas as entradas do usuário
   - Forneça mensagens de erro claras e úteis
   - Implemente logging detalhado
   - Trate erros de banco de dados
   - Gerencie arquivos corrompidos

4. **Interface de Linha de Comando**:
   - Use `argparse` para criar uma CLI amigável
   - Documente todos os comandos
   - Forneça feedback claro sobre o resultado das operações

### Exemplo de Uso:
```bash
# Adicionar uma tarefa
tarefas add "Revisar código Python" --data "2023-12-31"

# Listar tarefas pendentes
tarefas list --status pendente

# Marcar tarefa como concluída
tarefas concluir 1

# Exportar tarefas para JSON
tarefas exportar tarefas.json
```

## Dicas para Resolução

1. **Para os Exercícios Básicos**:
   - Comece definindo claramente os casos de teste
   - Use `try/except` para capturar exceções específicas
   - Crie exceções personalizadas quando necessário

2. **Para os Exercícios Intermediários**:
   - Considere o uso de context managers (`with`)
   - Implemente retentativas para operações de rede
   - Valide todos os dados de entrada

3. **Para os Exercícios Avançados**:
   - Use o módulo `logging` para registro de eventos
   - Implemente padrões como Circuit Breaker para chamadas de API
   - Considere o uso de filas para processamento assíncrono

4. **Para o Projeto Final**:
   - Comece com um MVP mínimo
   - Adicione tratamento de erros incrementalmente
   - Documente todas as exceções que cada função pode levantar
   - Escreva testes automatizados para os casos de erro

## Recursos Adicionais

1. [Documentação oficial sobre exceções em Python](https://docs.python.org/3/tutorial/errors.html)
2. [Logging em Python - Documentação](https://docs.python.org/3/howto/logging.html)
3. [Pytest - Framework de testes](https://docs.pytest.org/)
4. [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/)
5. [Design Patterns para Tratamento de Erros](https://refactoring.guru/design-patterns/error-handling)

Lembre-se que um bom tratamento de erros não é apenas capturar exceções, mas também fornecer informações úteis para diagnóstico e recuperação.
