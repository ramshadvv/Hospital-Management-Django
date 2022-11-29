from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.
class departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()

    def __str__(self):
        return self.dep_name

class doc(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doc')

    def __str__(self):
        return 'Dr  ' + self.doc_name + '- (' + self.doc_spec + ')'

class bookings(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(doc, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name

class contactus(models.Model):
    c_name = models.CharField(max_length=255)
    c_email = models.EmailField()
    c_msg = models.TextField()    
    msg_on = models.DateField(auto_now=True)
    def __str__(self):
        return self.c_name
