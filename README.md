<h1 align="center">App PyBurguer - Django e Bootstrap</h1>

<p>Projeto desenvolvido em acompanhamento ao curso gratuito da Udemy "Django 4 e Bootstrap 5 em 120 minutos". O objetivo foi estudar o uso do Django para construir uma API Rest. O resultado foi um site para venda de Hamburguers.</p>


# Índice

* [Status do projeto](#Status-do-projeto)
* [Tecnologias utilizadas](#Tecnologias-utilizadas)
* [Conceitos trabalhados](#conceitos-trabalhados)
* [Configuração do ambiente de teste](#Configuração-do-ambiente-de-teste)
* [Referências](#Referências)


# Status do projeto

🚧 Em desenvolvimento 🚧


# Tecnologias utilizadas

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/start/)
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)


# Conceitos trabalhados

* Aplicação de padrão de projeto MTV (Model Template View)
* CRUDs com Django Admin
* Criar layouts de páginas com Bootstrap
* Criação de templates reutilizáveis
* Injeção de conteúdo HTML
* Roteamento de arquivos estáticos


# Configuração do ambiente de teste

## Pré-requisitos

- **Python** versão 3 ou superior;


## Instalação

1. Faça o clone do repositório e no terminal navegue até a pasta.
2. Abra o seu editor de código e instale as dependências do projeto com `pip install -r requirements.txt`. O código foi desenvolvido no [Visual Studio Code](https://code.visualstudio.com).
3. Caso esteja usando o VSCode, configure o ambiente para trabalhar com o Django com os comandos `python3 -m venv .venv` e `source .venv/bin/activate`.
4. Caso deseje testar o CRUD (em desenvolvimento ainda), configure o banco de dados e o Admin do Django seguindo os passos do tópico abaixo, [Manipulando dados](#manipulando-dados).
5. Inicie o server de desenvolvimento executando o arquivo manage.py com o comando `python manage.py runserver`.
6. Para acessar o server basta copiar o endereço (IP + porta) obtido no terminal. Exemplo: `http://127.0.0.1:8000/`.


## Manipulando dados

1. Crie a estrutura do banco de dados. Rode o comando `python manage.py makemigrations` para criar os models e depois rode o comando `python manage.py migrate` para aplicar as migrations.
2. Crie um super-user com o comando `python manage.py createsuperuser`. Digite um valor para 'username' e 'password' e confirme a criação do usuário. O e-mail pode ser deixado em branco.
3. Para acessar o Admin do Django (e o banco de dados) basta navegar para o endpoint '/admin' (Exemplo: `http://127.0.0.1:8000/admin`) e informar as credenciais do super-user criado.


# Referências

Django 4 e Bootstrap 5 em 120 minutos:
https://www.udemy.com/course/django-em-120-minutos/learn/lecture/33482498#overview

Django Tutorial in Visual Studio Code:
https://code.visualstudio.com/docs/python/tutorial-django

Introduction - Bootstrap
https://getbootstrap.com/docs/4.4/getting-started/introduction/

How to return a static HTML file as a response in Django?
https://stackoverflow.com/questions/14400035/how-to-return-a-static-html-file-as-a-response-in-django

Fotos gratuitas de arquivo para baixar:
https://br.freepik.com/fotos-popular

Navbar - Bootstrap:
https://getbootstrap.com/docs/5.3/components/navbar/

Flex - Bootstrat:
https://getbootstrap.com/docs/4.0/utilities/flex/

Bootstrap row not occupying 100% width:
https://stackoverflow.com/questions/43741988/bootstrap-row-not-occupying-100-width