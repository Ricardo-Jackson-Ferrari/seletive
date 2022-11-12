from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from seletive.emprego.facade import get_experiencias, get_status

from .facade import (
    EmpresaDoesNotExist,
    excluir_empresa,
    get_empresa,
    get_empresas,
    get_nichos_mercado,
    get_tecnologias,
    registra_empresa,
)


def registro(request):
    if request.method == 'GET':
        ctx = {}
        ctx['title'] = 'Cadastro empresa'
        ctx['nichos_mercado'] = get_nichos_mercado()
        ctx['tecnologias'] = get_tecnologias()

        return render(request, 'empresa/registro.html', ctx)
    elif request.method == 'POST':
        data = {}
        data['nome'] = request.POST.get('nome').strip()
        data['email'] = request.POST.get('email').strip()
        data['cidade'] = request.POST.get('cidade').strip()
        data['endereco'] = request.POST.get('endereco').strip()
        data['nicho'] = request.POST.get('nicho').strip()
        data['caracteristicas'] = request.POST.get('caracteristicas').strip()
        data['tecnologias'] = request.POST.getlist('tecnologias')
        data['logo'] = request.FILES.get('logo')
        errors = []

        if (
            len(data['nome']) == 0
            or len(data['email']) == 0
            or len(data['cidade']) == 0
            or len(data['endereco']) == 0
            or len(data['nicho']) == 0
            or len(data['caracteristicas']) == 0
            or (not data['logo'])
        ):
            messages.error(request, 'Preencha todos os campos')
            return redirect('empresa:registro')

        file_size_limit = 10 * 1024 * 1024

        if data['logo'].size > file_size_limit:
            errors.append('A logo da empresa deve ter menos de 10MB')

        if errors:
            for error in errors:
                messages.error(request, error)

            return redirect('empresa:registro')

        registra_empresa(**data)

        messages.success(request, 'Empresa cadastrada com sucesso')

        return redirect('empresa:registro')


def listagem(request):
    ctx = {}
    ctx['title'] = 'empresas'
    ctx['empresas'] = get_empresas()
    ctx['tecnologias'] = get_tecnologias()

    tech_filter = request.GET.get('technology')
    name_filter = request.GET.get('name')

    if tech_filter:
        ctx['empresas'] = ctx['empresas'].filter(tecnologias=tech_filter)

    if name_filter:
        ctx['empresas'] = ctx['empresas'].filter(nome__icontains=name_filter)

    return render(request, 'empresa/listagem.html', ctx)


def excluir(request, id):
    excluir_empresa(id)
    messages.success(request, 'empresa excluída com sucesso')
    return redirect('empresa:listagem')


def detalhe(request, id):
    ctx = {}
    ctx['title'] = 'empresa | '

    try:
        ctx['empresa'] = get_empresa(id)
    except EmpresaDoesNotExist:
        raise Http404()

    ctx['empresas'] = get_empresas()
    ctx['tecnologias'] = get_tecnologias()
    ctx['nichos_mercado'] = get_nichos_mercado()
    ctx['experiencias'] = get_experiencias()
    ctx['status'] = get_status()

    return render(request, 'empresa/detalhe.html', ctx)
