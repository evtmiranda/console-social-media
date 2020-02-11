# Console Social Media

Esta aplicação é responsável por:

1. Identificar em um arquivo CSV qual a aplicação da categoria NEWS possui o maior número de avaliações;
2. Identificar em um arquivo CSV quais as 10 aplicações das categorias BOOK e MUSIC com o maior número de avaliações;
3. Consultar na API da aplicação de NEWS (twitter, facebook, medium e etc) quais das aplicações da categoria BOOK e MUSIC possuem o maior número de citações.
4. Salvar o resultado da consulta no formato JSON, csv e persistir em uma base de dados local.

## Como usar

Faça o download da aplicação e em seguida execute os comandos abaixo para instalar as dependências da aplicação:

Criação da virtualenv:

```
virtualenv venv
```

Ativação da virtualenv:

```
venv\Scripts\activate
```

Após o rodar o comando de ativação da virtualenv, instale os pacotes:

```
pip install python-dotenv requests
```

Após instalar os pacotes, crie um arquivo .env na pasta config. Existe um arquivo de exemplo na mesma pasta.

Depois de criar o arquivo .env, execute a aplicação:

```
python src/interfaceAdapters/console/start.py
```

A aplicação irá criar 3 arquivos na pasta resources:

database.db
result.csv
result.json
