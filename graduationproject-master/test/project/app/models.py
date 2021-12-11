from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    local = models.CharField('LOCAL', max_length=100, blank=False)
    rating = models.IntegerField()
    q1 = models.BooleanField(default=False)
    q2 = models.BooleanField(default=False)
    q3 = models.BooleanField(default=False)
    def __str__(self):
        return self.name