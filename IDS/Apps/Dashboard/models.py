from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class files(models.Model):
    file_name = models.FileField(upload_to='csvs')
    describe = models.TextField(max_length=200)                                                      
    uploaded = models.DateTimeField(auto_now_add=True)
    Results = models.TextField(default="")
    activated = models.BooleanField(default=False)


    def __str__(self):

        return f"File id: {self.id}"

class Recommend(models.Model):
    name = models.CharField(max_length=100)
    general = models.TextField( default="")
    host_level = models.TextField(default="")
    server_level = models.TextField(default="")
    in_the_organisation = models.TextField(default="")
    recommended_steps = models.TextField(default="")
    activated = models.BooleanField(default=True)

    
    def __str__(self): 

        return f"File id: {self.id}"

class Results(models.Model):
    key = models.CharField(max_length=100 ,default="")
    name = models.CharField(max_length=100)
    info = models.TextField()
    card_1_title = models.CharField(max_length=10)
    card_1_info = models.TextField()
    card_1_link = models.URLField()
    card_2_title = models.CharField(max_length=10)
    card_2_info = models.TextField()
    card_2_link = models.URLField()
    card_3_title = models.CharField(max_length=10)
    card_3_info = models.TextField()
    card_3_link = models.URLField()
    card_4_title = models.CharField(max_length=10)
    card_4_info = models.TextField()
    card_4_link = models.URLField()
    activated = models.BooleanField(default=True)

    
    def __str__(self):

        return f"File id: {self.id}"

    
class History(models.Model):

    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    result = models.CharField(max_length=100)
    description = models.TextField()
    recommendations = models.TextField()

    def __str__(self):
        return f"File id : {self.hist_id}"


class Contact(models.Model):

    
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20 , default="")
    img = models.ImageField(upload_to='profile',default='default.jpg')
    post = models.CharField(max_length=20)
    description = models.TextField()
    no = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"File id : {self.contact_id}"

