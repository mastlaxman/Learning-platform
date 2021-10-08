from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address= models.CharField(max_length=50)
    mobile = models.CharField(max_length = 15)
    status= models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name


class AutoField:
    pass