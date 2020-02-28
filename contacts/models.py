from django.db import models

class Contact(models.Model):
    class Meta:
        app_label = 'contacts'

    name = models.CharField(max_length=32)

# Create your models here.
