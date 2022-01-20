from django.db import models
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def publish(self):
        self.date_published = timezone.now()
        self.status = 1
        self.save()
