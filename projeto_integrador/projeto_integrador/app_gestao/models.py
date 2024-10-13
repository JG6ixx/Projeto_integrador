from django.db import models

class Usuarios(models.Model):
    ORGAO_CHOICES = [
        ('SSP', 'SSP'),
        ('PC', 'PC'),
    ]
    
    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=20)
    CPF = models.TextField(max_length=25)
    RG = models.TextField(max_length=25)
    Orgao = models.CharField(max_length=3, choices=ORGAO_CHOICES)  # Campo de escolha
    Emissao = models.DateField()
    Cidade_Nascimento = models.TextField(max_length=25)
    Estado = models.TextField(max_length=25)
    Data_Nascimento = models.DateField()
    Endereco = models.TextField(max_length=25)
    Setor_Bairro = models.TextField(max_length=25)
    Quadra = models.TextField(max_length=25)
    Lote = models.TextField(max_length=25)
    Apartamento = models.TextField(max_length=25)
    Complemento = models.TextField(max_length=25)
    Cidade = models.TextField(max_length=25)
    CEP = models.TextField(max_length=25)
    Telefone = models.TextField(max_length=25)
    Email = models.TextField(max_length=25)
    Sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)  # Campo de escolha
    documento = models.FileField(upload_to='documentos/')


    def __str__(self):
        return self.nome

    
    

class Curso(models.Model):
    pass


class SorteioCandidato(models.Model):
    pass

class MatriculaAluno(models.Model):
    pass