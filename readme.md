# Criação de uma plataforma de cursos utilizando framework Django

*Projeto realizado no módulo Django Web do Bootcamp Back-End Python e Django da [WoMakers Code](https://www.maismulheres.tech/).*

O projeto consiste na criação de uma página Web de cursos, com foco no cadastro dos cursos na plataforma.

## 💻 Tecnologias utilizadas:
* [Visual Studio Code](https://code.visualstudio.com/)
* [Python](https://www.python.org/)
* [Django](http://djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)

## ⚙ Instalações e Configurações:

```
#Instalando o ambiente virtual:

pip install virtualenv


#Criação do ambiente virtual:

py -3 -m venv [nome_do_ ambiente]


#Ativação do ambiente virtual:

.\[nome_do_ambiente]\Scripts\activate

    
#Instalação do Framework Django:

pip install django


#Criação do projeto e dos arquivos de configuração gerais:

django-admin startproject [nome_do_projeto] .


#Comando para rodar o servidor local:

python manage.py runserver


#Criação do novo aplicativo e suas funcionalidades:

python manage.py startapp [nome_do_app]


#Instalação do bootstrap:

pip install django-bootstrap-v5    
# incluir em settings -> installed_apps -> 'bootstrap5'


#Comandos para quando houver alteração em models (db):

python manage.py makemigrations
python manage.py migrate


#Criação de usuário(admin):

python manage.py createsuperuser


#Instalação do servidor Redis:

pip install redis


#Instalação do Django REST Framework:

pip install djangorestframework
```

## 📁 Conteúdo do repositório:
1. Models, forms, views, admin etc em Python;
2. Templates das páginas em HTML;
3. Banco de dados SQLite;
4. Anotações das instruções.