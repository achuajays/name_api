from django.db import models

class name(models.Model):
    name_1 = models.CharField(max_length = 100) 

    def __str__(self):
        return self.name_1