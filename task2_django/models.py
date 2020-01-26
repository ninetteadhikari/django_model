from django.db import models


# questions: how to add enums, how to add arrays, difference between text and charfield, add location

class Groups (models.Model):
    group_name = models.CharField(max_length=100)
    description= models.TextField()
    cover=models.CharField(max_length=200)
    icon=models.CharField(max_length=200)
    member_count=models.IntegerField()
    permissions=models.TextField()
    privacy=models.TextField()

class Users (models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    address=models.TextField()
    gender=models.CharField(max_length=50)
    birthday=models.DateField()
    groups = models.ManyToManyField(Groups,blank=True)

# class Posts (models.Model):
# class Comments (models.Model):
# class Replies (models.Model):