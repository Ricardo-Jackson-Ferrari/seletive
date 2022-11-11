from django.db import transaction

from .models import Empresa as _Empresa
from .models import NichoMercado as _NichoMercado
from .models import Tecnologia as _Tecnologia

EmpresaDoesNotExist = _Empresa.DoesNotExist
MarketNicheDoesNotExist = _NichoMercado.DoesNotExist
TechnologyDoesNotExist = _Tecnologia.DoesNotExist


def get_nichos_mercado():
    return _NichoMercado.objects.all()


def get_tecnologias():
    return _Tecnologia.objects.all()


def get_empresas():
    return _Empresa.objects.all()


def get_empresa(id):
    return get_empresas().get(id=id)


@transaction.atomic
def registra_empresa(
    nome, email, cidade, endereco, nicho, caracteristicas, tecnologias, logo
):
    empresa = _Empresa(
        nome=nome,
        email=email,
        cidade=cidade,
        endereco=endereco,
        nicho_mercado_id=int(nicho),
        caracteristicas=caracteristicas,
        logo=logo,
    )

    empresa.save()

    empresa.tecnologias.add(*tecnologias)

    empresa.save()

    return empresa


def excluir_empresa(id):
    _Empresa.objects.get(id=id).delete()
