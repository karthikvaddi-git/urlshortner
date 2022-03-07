from django.db import models

# Create your models here.
class qrcodemodel(models.Model):
    name=models.URLField(max_length=200)
    qrimage=models.ImageField(upload_to='images/')


    def __str__(self):
        return str(self.name)

