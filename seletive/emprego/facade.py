from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Emails as _Emails
from .models import Emprego as _Emprego
from .models import Tarefa as _Tarefa

EmpregoDoesNotExist = _Emprego.DoesNotExist
TarefaDoesNotExist = _Tarefa.DoesNotExist


def get_experiencias():
    return _Emprego.level_experiencia.field.flatchoices


def get_status():
    return _Emprego.status.field.flatchoices


def get_emprego(id):
    return _Emprego.objects.get(id=id)


def create_tarefa(emprego, titulo, prioridade, data):
    tarefa = _Tarefa(
        emprego_id=emprego, titulo=titulo, prioridade=prioridade, data=data
    )
    tarefa.save()

    return tarefa


def get_tarefas_emprego(id_emprego):
    return _Tarefa.objects.filter(emprego_id=id_emprego).filter(
        realizada=False
    )


def get_tarefa(id_tarefa):
    return _Tarefa.objects.get(id=id_tarefa)


def realizar_tarefa(id_tarefa):
    tarefa = _Tarefa.objects.get(id=id_tarefa)
    tarefa.realizada = True
    tarefa.save()

    return tarefa


@transaction.atomic
def create_emprego(
    empresa,
    email,
    titulo,
    tecnologias_dominadas,
    tecnologias_estudar,
    level_experiencia,
    data_final,
    status,
):
    emprego = _Emprego(
        empresa_id=empresa,
        email=email,
        titulo=titulo,
        level_experiencia=level_experiencia,
        data_final=data_final,
        status=status,
    )

    emprego.save()

    emprego.tecnologias_dominadas.add(*tecnologias_dominadas)
    emprego.tecnologias_estudar.add(*tecnologias_estudar)

    emprego.save()

    return emprego


def prepara_email_emprego(assunto, corpo, emprego):
    html_content = render_to_string(
        'emprego/template_email.html', {'corpo': corpo}
    )
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        assunto,
        text_content,
        settings.EMAIL_HOST_USER,
        [
            emprego.email,
        ],
    )

    email.attach_alternative(html_content, 'text/html')

    return email


def envia_email_emprego(assunto, corpo, emprego):
    email = prepara_email_emprego(assunto, corpo, emprego)

    result = email.send()

    mail = _Emails(
        assunto=assunto, emprego=emprego, corpo=corpo, enviado=False
    )

    if result:
        mail.enviado = True

    mail.save()

    return result


def get_emprego_emails(id_emprego):
    return _Emails.objects.filter(emprego_id=id_emprego)
