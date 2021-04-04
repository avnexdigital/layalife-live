from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, null=True, blank=True)
    dateofbirth = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    blank1 = models.TextField( max_length=122, null=True, blank=True)
    blankw = models.TextField(max_length=122,  null=True, blank=True)
    blankh = models.TextField(max_length=122, null=True, blank=True)
    blankf = models.TextField(max_length=122, null=True, blank=True)
    blanki = models.TextField(max_length=122, null=True, blank=True)
    blanks = models.TextField(max_length=122, null=True, blank=True)
    blankv = models.TextField(max_length=122, null=True, blank=True)
    blankg = models.TextField(max_length=122, null=True, blank=True)
    blankn = models.TextField(max_length=122, null=True, blank=True)
    blankt = models.TextField(max_length=122, null=True, blank=True)
    blanke = models.TextField(max_length=122, null=True, blank=True)

    date = models.DateField()

    def __str__(self):
        return self.name


