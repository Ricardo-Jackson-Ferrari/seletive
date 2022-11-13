<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://code.djangoproject.com/raw-attachment/ticket/24953/django-hexbin.png" width="200" alt="Django Logo" /></a>
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>
</p>


<hr>

<a id="-tecnologias"></a>

## Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

<hr>

<a id="-projeto"></a>

## 💻 Projeto

O projeto Seletive é uma ideia de aplicação desenvolvida para pessoas que procuram uma forma de organizar as vagas de emprego as quais tem interesse, a plataforma tem como objetivo facilitar essa ação.

<p align="center">
  <img alt="Página inicial" src=".github/media/pagina_inicial.jpg" width="100%">
</p>

<p align="center">
  <img alt="Cadastro empresa" src=".github/media/cadastro_empresa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Página empresa" src=".github/media/pagina_empresa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Cadastro vaga" src=".github/media/cadastro_vaga.jpg" width="100%">
</p>

<p align="center">
  <img alt="Pagina vaga" src=".github/media/pagina_vaga.jpg" width="100%">
</p>

<p align="center">
  <img alt="Cadastro tarefa" src=".github/media/cadastro_tarefa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Envio de email" src=".github/media/envio_email_vaga.jpg" width="100%">
</p>

<a id="-como-executar"></a>

## 🚀 Como executar

### 💻 Pré-requisitos
 **Antes de começar, verifique se você atendeu aos seguintes requisitos:**

- Você tem uma máquina `< Windows / Linux / Mac >`.

- Você tem python na versão 3.11 ou superior instalado em sua máquina.


### Como instalar localmente:

- clone ou baixe o repositório.

Com o ambiente virtual ativo:

- Acesse a pasta do projeto no terminal execute:

```console
cd seletive
cp env .env
python -m pip install poetry
poetry install
```

**OBS. Não se esqueça de alterar o arquivo .env que foi gerado a partida da cópia de exemplo "env" que vem na raíz do projeto.**

### Para total funcionamento da aplicação ainda é necessário fazer as migrações para gerar o esquema de banco de dados:

```console
python manage.py migrate
``` 

### Criando um usuário para acessar o painel de administração:

```console
python manage.py createsuperuser
```

## 👨‍💻 Ativando a aplicação (localmente)
Para executar o servidor localmente (Com o ambiente virtual ativo):

```console
python manage.py runserver
```

Agora é possível acessar a aplicação em http://localhost:8000/
