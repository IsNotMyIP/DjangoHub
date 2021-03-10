from django.db import models
from django.utils import timezone
# Create your models here.
class Cigar(models.Model):
    pub_date = models.DateTimeField("Fecha", default=timezone.now)
    stopped = models.IntegerField("evitado")

    def __str__(self):
        return str(self.pub_date)