from django.db import models

# Create your models here.
class Base(models.Model):
    criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    atualizacao = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Curso(Base):
    titulo = models.CharField('Título', max_length=100)
    url = models.URLField('URL', max_length=200)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso', related_name='avaliacoes')
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    avaliacao = models.DecimalField('Avaliação', max_digits=3, decimal_places=1, default="")

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.nome}, {self.avaliacao} estrelas'