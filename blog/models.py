from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    """Post a blog entry"""

    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        """Publish a blog entry """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
