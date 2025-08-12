Projeto: Teste de Estresse Simples
Simular muitas requisições concorrentes para um endpoint/API, serviço ou função, medindo se o sistema aguenta a carga e onde ele quebra.

✅ Passos para um teste de estresse simples do zero
1. Defina o alvo
Qual será testado? Um endpoint HTTP? Uma função local? Um banco?

Exemplo: http://localhost:8000/usuarios

2. Implemente um cliente que faz requisições
Use urllib ou http.client (nativos).

O cliente deve ser capaz de fazer uma requisição e armazenar tempo de resposta e status.

3. Simule concorrência com threading ou multiprocessing
Crie múltiplas threads ou processos para disparar as requisições ao mesmo tempo.

Teste com 10, 100, 1000 simultâneos.

4. Controle o volume e o tempo
Faça cada worker enviar N requisições (ex: 100 por thread).

Rode por X segundos ou até atingir o total desejado.

5. Registre resultados
Conte requisições bem-sucedidas e com erro.

Meça o tempo total, tempo médio, maior e menor tempo de resposta.

Use timestamps para gerar um log.

6. Identifique gargalos e falhas
Se o sistema começar a dar timeout, erro 500 ou ficar lento demais, anote:

número de threads

total de requisições

quando a falha começou

7. Repita com mais carga
Aumente gradualmente as threads e repita.

Observe onde o sistema satura ou falha.

🧪 Exemplo de cenário prático:
100 threads

Cada uma faz 50 requisições para http://localhost:5000/api/teste

Medir tempo de cada resposta

Contar quantas deram erro ou timeout