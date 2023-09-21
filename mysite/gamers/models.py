from django.db import models

from mysite.models import BaseModel


class GAMER_USER(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'
