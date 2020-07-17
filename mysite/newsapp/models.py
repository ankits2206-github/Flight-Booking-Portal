from django.db import models

# Create your models here.

class news(models.Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"


class country(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
