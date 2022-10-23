#Django
from django.db import models

class Tag(models.Model):
    """ django data model tag """
    
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """ django data model post """
    
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField('content')
    tag = models.ManyToManyField(
        Tag,
        verbose_name = 'tag'
    )

    created_at = models.DateTimeField("date published")
    updated_at = models.DateTimeField("date updated")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
