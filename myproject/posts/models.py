from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(blank=True, null=True, verbose_name='description')
    slug = models.SlugField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'My Post'