from django.db import models


# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=40)
    confrom_pass = models.CharField(max_length=40)

    def __str__(self):
        return self.username
