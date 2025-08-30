from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True, help_text="Apenas dígitos")
    matricula = models.CharField(max_length=30, unique=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "colaborador"
        ordering = ["nome"]
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
