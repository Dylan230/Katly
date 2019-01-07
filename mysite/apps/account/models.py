from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    CHOICES = (('Profesor', 'Profesor'), ('Alumno', 'Alumno'))
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.rol


class Work(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=140)
    group = models.CharField(max_length=5)
    archive = models.FileField()

    def __str__(self):
        return self.title

class WorkResponse(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    user_response = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=140)
    group = models.CharField(max_length=5)
    archive = models.FileField()

    def __str__(self):
        return self.title

class AddToGroup(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    user_add = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Group(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    user = instance
    if created:
        account = Account(user=user)
        account.save()
