# carros

dentro da pasta do projeto para criar uma venv
python -m venv venv


ativar venv
-- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  --primeira ativacao
-- venv\Scripts\activate

pip install django
django-admin startproject app .
obs:o ponto no final eh para criar na pasta que ja estou

python manage.py runserver
para rodar o projeto

criando uma app dentro do projeto
python manage.py startapp cars

em app settings.py , configurar  em INSTALLED_APPS nosso app cars criado
criando as migracoes do django
python manage.py makemigrations -- se nao tiver nao vai nenhuma migracao

criando as tabelas do django 
python manage.py migrate

criando superusuario no django
python manage.py createsuperuser

criando o arquivo de dependencias
pip freeze > requirements.txt
depois basta executar
pip install -r requirements.txt

adicionando o campo images no python precisa instalar o Pillow
python -m pip install Pillow

para melhor visualizacao das pastas instalei no vscod 
material icon theme
