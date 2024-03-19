from typing import Any
from django.db import models
from user.models import *
from django.core.validators import FileExtensionValidator

class letter(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    path = models.FileField(upload_to='letter/%D', validators=[FileExtensionValidator(['html'])])
    image = models.ImageField(upload_to='image/%D')
    creater = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    
    
    def __str__(self) -> str:
        return self.name

