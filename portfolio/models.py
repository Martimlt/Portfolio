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

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ranking = models.IntegerField()
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    professorAuxiliar = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+')   
    linklusofona = models.URLField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"

class Mestrado(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    trimestre = models.IntegerField() # 1 -> Summer
    units = models.IntegerField()
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+')
    order = models.IntegerField()

    def __str__(self):
        return f"{self.nome}" 

class Competencia(models.Model):
    competencia = models.CharField(max_length=50)
    valor = models.IntegerField()
    softskill = models.BooleanField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.competencia}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    linkGit = models.URLField(max_length=500)
    cadeira = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, blank=True)
    lecture = models.ForeignKey(Mestrado, on_delete=models.CASCADE, blank=True)
    ano = models.IntegerField()
    semestre = models.IntegerField(blank=True)
    trimestre = models.IntegerField(blank=True)
    imagem = models.ImageField()
    tecnologia = models.CharField(max_length=100)
    participante = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='+', blank=True)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name='+')
    video = models.URLField(blank=True)
    left = models.BooleanField(default=False)
    right = models.BooleanField(default=False)
    mestrado = models.BooleanField(default=False)
    licenciatura = models.BooleanField(default=False)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.titulo}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        error_messages={
            'invalid': 'Please enter a valid email address.',
        }
    )
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name