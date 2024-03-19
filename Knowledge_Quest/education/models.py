from django.db import models


# Create your models here.
class Resource(models.Model):
    def __str__(self): 
        return self.title

    title = models.CharField(max_length =50)
    desc_1= models.CharField(max_length = 700)
    desc_2= models.CharField(max_length = 700)
    desc_3= models.CharField(max_length = 700)
    



class FeedBack(models.Model):
    def _str_(self):
        return self.Feedback

    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



