from django.db import models



class contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=80,default='')
    phone=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=500,default='')

    def __str__(self) :
        return self.name
        


# Create your models here.
