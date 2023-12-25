from django.db import models

# Create your models here.

class Pessoa(models.Model):
    primeiroNome = models.CharField(max_length=100)
    ultimoNome = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=500)
    outroLink = models.URLField(max_length=500)
    professor = models.BooleanField(default=False)
    aluno = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.primeiroNome} {self.ultimoNome}"

class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ranking = models.IntegerField()
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    professorAuxiliar = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+')   
    linklusofona = models.URLField()

    def __str__(self):
        return f"{self.nome}"

class Competencia(models.Model):
    competencia = models.CharField(max_length=50)
    valor = models.IntegerField()
    softskill = models.BooleanField()

    def __str__(self):
        return f"{self.competencia}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    linkGit = models.URLField(max_length=500)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    ano = models.IntegerField()
    imagem = models.ImageField()
    tecnologia = models.CharField(max_length=100)
    participante = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+')
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name='+')
    video = models.URLField(blank=True)
    left = models.BooleanField(default=False)
    right = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo}"