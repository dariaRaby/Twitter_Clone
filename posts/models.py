from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table='post'

    name = models.CharField(
        "Name",blank=False,null=False,max_length=16,db_index=True,default="Anonymous"
    )
    body = models.CharField(
        'Body', blank=False,null=False,max_length=140,db_index=True,default="Type the text"

    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True

    )
    image = CloudinaryField(
        'image', blank = True, db_index= True

    )
    likes =  models.PositiveIntegerField(
        'Likes', default=0, null=True, blank=True
    )
