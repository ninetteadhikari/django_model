from django.db import models


# questions: how to add enums, how to add arrays, difference between text and charfield, add location

class Groups (models.Model):
    group_name = models.CharField(max_length=100)
    description= models.TextField()
    cover=models.ImageField()
    icon=models.ImageField()
    member_count=models.IntegerField()
    permissions=models.CharField()
    privacy=models.TextField()
    users = models.ManyToManyField('task2_django.Users',blank=True)

    def __str__(self):
        return self.group_name

class Users (models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    address=models.TextField()
    gender=models.CharField(max_length=50)
    birthday=models.DateField()
    
    def __str__(self):
        return self.name

class Posts (models.Model):
    group=models.ForeignKey(Groups,blank=True,null=True, on_delete=models.SET_NULL)
    # another on_delete option is called SET_DEFAULT
    user=models.ForeignKey(Users, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_description

# class Comments (models.Model):
# class Replies (models.Model):