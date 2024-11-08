# Web Link Extractor API Load Testing

Este repositório contém scripts e configurações para testar a carga de APIs de extração de links da web usando ferramentas como Locust e Jupyter Notebooks para análise de resultados.

## Configuração

### Pré-requisitos

- Docker
- Docker Compose
- Python 3.12.0
- Ruby

### Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/pedrxlz/web-link-extractor-api-load-testing.git
   cd web-link-extractor-api-load-testing
   ```

2. Construa e inicie os containers Docker:
   ```sh
   docker-compose up --build
   ```

## Estrutura dos Logs

Os logs de extração são armazenados no arquivo `logs/extraction.log`. Cada linha do log contém um timestamp, o status da requisição (HIT ou MISS) e a URL acessada.

## Scripts

### Python API

- `python-api/main.py`: Implementação da API em Python.
- `python-api/entrypoint.sh`: Script de entrada para o container Docker da API Python.

### Ruby API

- `ruby-api/linkextractor.rb`: Implementação da API em Ruby.
- `ruby-api/entrypoint.sh`: Script de entrada para o container Docker da API Ruby.
