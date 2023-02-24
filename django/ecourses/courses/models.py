from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.conf import settings
class ItemBase(models.Model):
    class Meta: #không tạo bảng chỉ làm thuộc tính
        abstract = True  
    subject = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default= None)
    #MEDIA_ROOT + upload_to
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
       return f'{self.subject}'


# tạo ra user người dùng (AbstractUser)
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    #objects = EmailUserManager()



class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    def __str__(self):
        return self.name

    
class Couser(ItemBase):
    class Meta: # không được phép trùng dữ liệu
        unique_together = ('subject', 'Category')
        ordering = ["-id"]
    description = models.TextField(null=True, blank= True)
    Category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True)



class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'Couser')
    content = RichTextField()
    Couser = models.ForeignKey(Couser, on_delete=models.CASCADE, related_name='lessons')
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    content = RichTextField()
    lesson = models.ForeignKey(Lesson, on_delete= models.SET_NULL, related_name='comment',null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,null=True)

    