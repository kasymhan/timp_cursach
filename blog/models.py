from django.db import models


# Create your models here.\
class Contacts(models.Model):
    phone_number = models.TextField(max_length=12)
    email = models.EmailField()


class Acconts(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    authecation = models.BooleanField(default=False)
    file_l = models.ImageField()


class User(models.Model):
    Name = models.TextField(max_length=100)
    contact = models.OneToOneField(Contacts, on_delete=models.CASCADE)
    account = models.OneToOneField(Acconts, on_delete=models.CASCADE, null=True)


class Announcement(models.Model):
    Name = models.CharField(max_length=100)
    accounts = models.ForeignKey(Acconts, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    inform = models.TextField(blank=True)
    price = models.IntegerField()
    file_l = models.ImageField(null=True)
