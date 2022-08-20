from django.db import models

# Create your models here.
class Certificate(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    event= models.CharField(max_length=4)
    hours= models.CharField(max_length=20)
    kilometers = models.CharField(max_length=20)
    top_effort = models.CharField(max_length=20)
    top=models.BooleanField(default=False)
    
    USERNAME_FIELD ='name'
    REQUIRED_FIELDS = ['gender','event','hours','kilometers','top_effort','top']
    
    def __str__(self):
        return self.name