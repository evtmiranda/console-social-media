# Console Social Media

Esta aplicação é responsável por:

1. Identificar em um arquivo CSV qual a aplicação da categoria NEWS possui o maior número de avaliações;
2. Identificar em um arquivo CSV quais as 10 aplicações das categorias BOOK e MUSIC com o maior número de avaliações;
3. Consultar na API da aplicação de NEWS (twitter, facebook, medium e etc) quais das aplicações da categoria BOOK e MUSIC possuem o maior número de citações.
4. Salvar o resultado da consulta nos formatos JSON, CSV e persistir em uma base de dados local.

## Instalação dos pacotes

Faça o download da aplicação e em seguida execute os comandos abaixo na pasta raiz do projeto para instalar as dependências da aplicação:

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

## Configuração do ambiente

Crie um arquivo .env na pasta config. Existe um arquivo de exemplo na mesma pasta.

Caso a variável APP_ENVIRONMENT esteja configurada como "development" a aplicação irá usar um objeto json mockado, para não consumir a API do twitter. Se a variável conter qualquer outro valor, então a API do twitter será chamada.

Para realizar as consultas no twitter é necessário informar os dados de autenticação através das variáveis TWITTER_KEY e TWITTER_SECRET_KEY presentes no arquivo .env.

## Rodando a aplicação

Para rodar a aplicação execute o comando abaixo a partir da pasta raiz do projeto:

```
python src/interfaceAdapters/console/start.py
```

A aplicação irá criar 3 arquivos na pasta resources:

* database.db
* result.csv
* result.json
