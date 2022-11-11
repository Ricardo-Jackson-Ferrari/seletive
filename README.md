# **Controle de inscrições em empregos**

*Desenvolvido usando Django*

> ## Descrição
>
>Aplicação web para controle de inscrições em empregos, a aplicação não tem controle de acesso, então tem como propósito ser usada por um único usuário.

> ## Funcionalidades
>
> - Cadastro de empresa
>
> - Cadastro de emprego
>
> - Cadastro de tarefas relacionadas ao emprego
>
> - Envio de email para contato do emprego(configurado para console)


>## Como instalar localmente (supondo que você tenha git e python >= 3.11 instalado):
>
>clone ou baixe o repositório e instale instale as dependencias.
>
>Com o ambiente virtual ativo:

### Caso use o git
```console
git clone https://github.com/Ricardo-Jackson-Ferrari/seletive.git
```

### Na cópia do repositório
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

### Criando um usuário com acesso ao admin:

```console
python manage.py createsuperuser
```

>## Ativando a aplicação (localmente)
>Para executar o servidor localmente (Com o ambiente virtual ativo):

```console
python manage.py runserver
```

Agora é possível acessar a aplicação em http://localhost:8000/empresa
