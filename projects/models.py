from django.db import models
import uuid  # means unique id


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # blank mean form could be empty
    demo_link = models.CharField(null=True, blank=True, max_length=2000)
    source_link = models.CharField(max_length=20000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)  # str used because class bellow
    vote_total = models.IntegerField(default=0, null=True, blank=True)  # total vote on review class
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # automatice created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)  # uuid4 encoding type

    def __str__(self):
        return self.title


class Review(models.Model):  # One to Many relationship
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):  # Many to Many relationship
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # automatice created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
