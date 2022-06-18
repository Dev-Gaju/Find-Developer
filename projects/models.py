from django.db import models
import uuid  #means unique id


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  #blank mean form could be empty
    demo_link = models.CharField(null=True, blank=True,max_length=2000)
    source_link = models.CharField(max_length=20000, null=True, blank=True)
    created=  models.DateTimeField(auto_now_add=True)  #automatice created
    id = models.UUIDField(default=uuid.uuid4(), unique=True, primary_key=True, editable=False)   #uuid4 encoding type



    def __str__(self):
        return self.title

