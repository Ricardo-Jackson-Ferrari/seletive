from django.db import models

from seletive.empresa.models import Empresa, Tecnologia


class Emprego(models.Model):
    choices_experiencia = (
        ('E', 'Estágio'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior'),
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado'),
    )

    empresa = models.ForeignKey(
        Empresa,
        null=True,
        on_delete=models.SET_NULL,
    )
    titulo = models.CharField(max_length=30, verbose_name='título')
    level_experiencia = models.CharField(
        max_length=2,
        choices=choices_experiencia,
        verbose_name='nível de experiência',
    )
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologia)
    tecnologias_estudar = models.ManyToManyField(
        Tecnologia, related_name='study', verbose_name='tecnologias a estudar'
    )
    email = models.EmailField()

    def progresso(self):
        status_porcentagem = [
            ((i + 1) * 20, j[0]) for i, j in enumerate(self.choices_status)
        ]
        status_porcentagem_atual = list(
            filter(lambda x: x[1] == self.status, status_porcentagem)
        )[0][0]
        return status_porcentagem_atual

    def __str__(self):
        return self.titulo


class Tarefa(models.Model):
    choices_prioridade = (
        ('B', 'baixa'),
        ('A', 'alta'),
        ('U', 'urgente'),
    )
    emprego = models.ForeignKey(Emprego, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    prioridade = models.CharField(max_length=1, choices=choices_prioridade)
    data = models.DateTimeField()
    realizada = models.BooleanField(default=False)

    def prioridade_cor(self):
        match self.prioridade:
            case 'B':
                cor = 'verde'
            case 'A':
                cor = 'amarelo'
            case _:
                cor = 'vermelho'

        return cor

    def __str__(self):
        return self.titulo


class Emails(models.Model):
    emprego = models.ForeignKey(Emprego, on_delete=models.DO_NOTHING)
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.assunto
