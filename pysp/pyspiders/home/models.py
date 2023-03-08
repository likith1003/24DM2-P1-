from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(("Name"), max_length=50)
    pno=models.CharField(("Pno"), max_length=50)
    email=models.EmailField(("Email"), max_length=254)
    feedback=models.CharField(("Feedback"), max_length=50)
    date=models.DateField(("Date"), auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name
    