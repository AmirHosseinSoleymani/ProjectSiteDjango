from django.db import models


class News(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name + "  : '" + self.email + "'"