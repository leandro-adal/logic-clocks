# Logic clocks - Lamport

# Description:
- Projeto da disciplina de Sistemas Distribuídos que tem por objetivo mostra o funcionamento do algoritmo de Lamport em relógios lógicos.
- O projeto usa o `gRPC` como forma de comunicação.
- Em `clock_server` o servidor é "ligado"
- `update_time_service` herda do service do gRPC sendo responsável por fazer a verificação do tempo logico do relógio.
- Por fim, `clock_client` é o lado cliente

## Rodando o projeto

Para o roda o cliente simples:

- 1 - Executar o clock_server

- 2 - Executar o clock_client