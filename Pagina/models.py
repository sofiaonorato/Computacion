from django.db import models
from django.utils import timezone

class Procesador(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200)
    caracteristica = models.TextField()
    precio = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.modelo