from django.db import models


class Tecnologia(models.Model):
    nome = models.CharField(max_length=30, verbose_name='tecnologia')

    def __str__(self):
        return self.nome


class NichoMercado(models.Model):
    nicho_mercado = models.CharField(
        max_length=30, verbose_name='nicho de mercado'
    )

    def __str__(self):
        return self.nicho_mercado


class Empresa(models.Model):
    logo = models.ImageField(upload_to='logo_empresa', null=True, blank=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologia)
    endereco = models.CharField(max_length=60, verbose_name='endereço')
    nicho_mercado = models.ForeignKey(
        to=NichoMercado,
        on_delete=models.DO_NOTHING,
        verbose_name='nicho de mercado',
    )
    caracteristicas = models.TextField(verbose_name='características')

    def __str__(self):
        return self.nome
