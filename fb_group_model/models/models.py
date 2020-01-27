from django.db import models


class Groups (models.Model):
    group_name = models.CharField(max_length=100)
    description= models.TextField()
    cover_photo=models.ImageField()
    icon=models.ImageField()
    member_count=models.IntegerField()
    users = models.ManyToManyField('models.Users',blank=True)

    def __str__(self):
        return self.group_name

class Users (models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    address=models.TextField()
    gender=models.CharField(max_length=50)
    birthday=models.DateField()
    email= models.EmailField()
    relationship_status=models.CharField(max_length=50)
    profile_picture=models.ImageField()
    friends=models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    created_date=models.DateTimeField()
    
    def __str__(self):
        return self.name

class Photos (models.Model):
    group_photos=models.ImageField()
    group=models.ForeignKey(Groups,blank=True, on_delete=models.CASCADE)
    user=models.ForeignKey(Users, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.group_photos

class Posts (models.Model):
    post_description=models.TextField()
    likes_count=models.IntegerField()
    created_date=models.DateTimeField()
    group=models.ForeignKey(Groups,blank=True,null=True, on_delete=models.SET_NULL)
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_description

class Likes (models.Model):
    likes=models.BooleanField()
    post=models.ForeignKey(Posts, on_delete=models.CASCADE)
    user=models.ForeignKey(Users, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.likes

class Comments (models.Model):
    comment_description=models.TextField()
    created_date=models.DateTimeField()
    post=models.ForeignKey(Posts, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_description


class Replies (models.Model):
    reply_description=models.TextField()
    created_date=models.DateTimeField()
    comment=models.ForeignKey(Comments,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.reply_description
