from django.db import models


class Group (models.Model):
    group_name = models.CharField(max_length=100)
    description= models.TextField()
    cover_photo=models.ImageField(upload_to='coverphoto')
    icon=models.ImageField(upload_to='iconphoto')
    member_count=models.IntegerField()
    # members = models.ManyToManyField('models.User',blank=True)

    def __str__(self):
        return self.group_name

class GroupUser (models.Model):
    user=models.ForeignKey('models.User', null=True, on_delete=models.SET_NULL)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    join_date=models.DateTimeField()

def __str__(self):
        return self.user

class User (models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    address=models.TextField()
    gender=models.CharField(max_length=50)
    birthday=models.DateField()
    email= models.EmailField()
    relationship_status=models.CharField(max_length=50)
    profile_picture=models.ImageField(upload_to='profilephoto')
    friends=models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    created_date=models.DateTimeField()
    
    def __str__(self):
        return self.name

class Photo (models.Model):
    group_photos=models.ImageField(upload_to='photos')
    group=models.ForeignKey(Group,blank=True, on_delete=models.CASCADE)
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.group_photos

class Post (models.Model):
    post_description=models.TextField()
    likes_count=models.IntegerField()
    created_date=models.DateTimeField()
    group=models.ForeignKey(Group, blank=True,null=True, on_delete=models.SET_NULL)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    reply=models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.post_description

class Like (models.Model):
    likes=models.BooleanField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user=models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
    # comments=models.ForeignKey('models.Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.likes

# class Comment (models.Model):
#     description=models.TextField()
#     created_date=models.DateTimeField()
#     post=models.ForeignKey(Posts, blank=True, on_delete=models.CASCADE)
#     user=models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
#     reply=models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.description
