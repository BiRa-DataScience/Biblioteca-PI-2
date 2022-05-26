import uuid
from django.db import models


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


DIVISAO = (
    ('fundamental', 'Ensino Fundamental'),
    ('medio', 'Ensino Médio')
)

ITEM = (
    ('livro', 'Livro'),
    ('dvd', 'DVD/CD/BLUE-RAY'),
    ('jornal', 'Jornal'),
    ('revista', 'Revista')
)

SEXO = (
    ('f', 'Feminino'),
    ('m', 'Masculino')
)

ARMARIO = (
    ('A', 'Armário A'),
    ('B', 'Armário B'),
    ('C', 'Armário C')
)

PRATELEIRA = (
    ('1', 'Prateleira 1'),
    ('2', 'Prateleira 2'),
    ('3', 'Prateleira 3')
)


class Material(models.Model):
    material = models.CharField('Tipo do material', max_length=8, choices=ITEM)
    titulo = models.CharField('Titulo do material', max_length=200)
    autor = models.CharField('Autor', max_length=50)
    descricao = models.TextField('Descrição do material', max_length=1000)
    data = models.DateTimeField('Data de Registro', auto_now_add=True)
    armario = models.CharField('Localização do Livro no armário', max_length=8, choices=ARMARIO)
    prateleira = models.CharField('Localização do Livro na prateleira', max_length=8, choices=PRATELEIRA)
    posse = models.ForeignKey('core.Aluno', on_delete=models.CASCADE)
    dataposse = models.DateTimeField('Data de Registro do empréstimo', max_length=10, blank=True)

    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO)
    documento = models.CharField('Documento de identidade', max_length=12)
    divisao = models.CharField('Divisão educacional', max_length=11, choices=DIVISAO)
    email = models.EmailField('Email de contato', max_length=20)
    data = models.DateTimeField('Data de registro do cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome
