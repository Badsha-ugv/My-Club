from django.db import models
from user_account.models import CustomUser

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    project_name = models.CharField(max_length=500)
    project_description = models.TextField(default='')
    publish_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='project_image/',blank=True, null=True)
    

    def __str__(self):
        return self.project_name 

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True, blank=True)
    image  = models.ImageField(upload_to='project_image/',blank=True, null=True)


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_image/',null=True,blank=True)

class Award(models.Model):
    event_name = models.CharField(max_length=300)
    event_desc = models.TextField(blank=True,default='')
    image = models.ImageField(upload_to='award_image/',null=True,blank=True)
    
    event_date = models.DateTimeField()

    def __str__(self):
        return self.event_name
class AwardImage(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE,null=True, blank=True) 
    image = models.ImageField(upload_to='award_image/',null=True,blank=True)


#Gallery Image
class Image(models.Model):
    image = models.FileField(upload_to='image_gallery/',null=True)

    def __str__(self):
        return str(self.id) 



# Frontend People Model
class People(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    bio = models.TextField() 
    image = models.ImageField(upload_to='people_image/',null=True,blank=True)
    email = models.EmailField(max_length=140,blank=True,null=True)
    phone = models.CharField(max_length=15, blank=True,null=True) 

    def __str__(self):
        return self.name

#Project Comment 
class Comment (models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,blank=True)  
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True, blank=True)
    text = models.TextField(null=True, blank=True) 
    date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.text[:50]

