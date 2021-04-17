from django.db import models

# Create your models here.
class Users_tb(models.Model):
    #id akan dibuat sendiri oleh django
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Skill_tb(models.Model):
    #id akan dibuat sendiri oleh django
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(Users_tb, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
