from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .facade import (
    EmpregoDoesNotExist,
    TarefaDoesNotExist,
    create_emprego,
    create_tarefa,
    envia_email_emprego,
    get_emprego,
    get_emprego_emails,
    get_tarefa,
    get_tarefas_emprego,
    realizar_tarefa,
)


def only_method_post(view):
    def wrapper(request, *args, **kwargs):
        if request.method != 'POST':
            raise Http404()

        return view(request, *args, **kwargs)

    return wrapper


def registro(request):
    if request.method == 'POST':
        data: dict
        data['empresa'] = request.POST.get('empresa')
        data['email'] = request.POST.get('email')
        data['titulo'] = request.POST.get('titulo')
        data['tecnologias_dominadas'] = request.POST.getlist(
            'tecnologias_domina'
        )
        data['tecnologias_estudar'] = request.POST.getlist(
            'tecnologias_nao_domina'
        )
        data['level_experiencia'] = request.POST.get('experiencia')
        data['data_final'] = request.POST.get('data_final')
        data['status'] = request.POST.get('status')

        create_emprego(**data)

        return redirect('empresa:detalhe', id=data['empresa'])
    else:
        raise Http404()


def detalhe(request, id):
    try:
        emprego = get_emprego(id)
    except EmpregoDoesNotExist:
        raise Http404()
    ctx = {}
    ctx['titulo'] = 'Emprego | '
    ctx['emprego'] = emprego
    ctx['tarefas'] = get_tarefas_emprego(emprego.id)
    ctx['emails'] = get_emprego_emails(emprego.id)

    return render(request, 'emprego/detalhe.html', ctx)


def registro_tarefa(request, id_vaga):
    if request.method == 'POST':
        try:
            emprego = get_emprego(id_vaga)
        except EmpregoDoesNotExist:
            raise Http404()

        data = {}
        data['emprego'] = emprego.id
        data['titulo'] = request.POST.get('titulo')
        data['prioridade'] = request.POST.get('prioridade')
        data['data'] = request.POST.get('data')

        try:
            create_tarefa(**data)

            messages.success(request, 'Tarefa criada com sucesso!')
        except:
            messages.error(request, 'Ocorreu um erro ao cadastrar a tarefa.')

        return redirect('emprego:detalhe', id=id_vaga)
    else:
        raise Http404()


def realiza_tarefa(request, id_tarefa):
    if request.method == 'GET':
        try:
            tarefa = get_tarefa(id_tarefa)
        except TarefaDoesNotExist:
            raise Http404()

        realizar_tarefa(tarefa.id)

        messages.success(request, 'Tarefa realizada com sucesso!')

        return redirect('emprego:detalhe', id=tarefa.emprego.id)
    else:
        raise Http404()


@only_method_post
def envia_email(request, id_emprego):
    data = {}
    data['emprego'] = get_emprego(id_emprego)
    data['assunto'] = request.POST.get('assunto')
    data['corpo'] = request.POST.get('corpo')

    email_status = envia_email_emprego(**data)

    if email_status:
        messages.success(request, 'Email enviado com sucesso!')
    else:
        messages.error(request, 'Falha ao enviar o email.')

    return redirect('emprego:detalhe', id=id_emprego)
