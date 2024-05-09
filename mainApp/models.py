from django.db import models
from ckeditor.fields import RichTextField

class Speeche(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)+" "+self.title
    

class SliderBanner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/",)

    def __str__(self):
        return str(self.id)+" "+self.name
    
class OnLoadPopup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/",)

    def __str__(self):
        return str(self.id)+" "+self.name
    
class YouTubeVideo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    link = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.title
    
class MediaCoverage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)+" "+self.title
    
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)+" "+self.title
    
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)
    
class VideosGallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="uploads/")
    link = models.TextField(default="",null="true",blank="true")

    def __str__(self):
        return str(self.id)+" "+self.title
    
class DailyUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="uploads/",default="",null="true",blank="true")

    def __str__(self):
        return str(self.id)+" "+self.title
    
class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    email = models.EmailField(default="",null="true",blank="true")
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=1000)
    message = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name
    
class BusinessQueryDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    businessName = models.CharField(max_length=500,default="",null="true",blank="true")
    email = models.EmailField(default="",null="true",blank="true")
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=1000)
    location = models.CharField(max_length=500,default="",null="true",blank="true")
    query = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name
    
class NewsletterSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default="",null="true",blank="true")
    
    def __str__(self):
        return str(self.id)+" "+self.email