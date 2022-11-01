from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    donation_value = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, default='Uncategorized')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    imgs = models.ImageField(null=True, blank=True, default='nta-logo_-_Copy_4_-_Copy.png', upload_to="media")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def num_likes(self):
        return self.liked.all().count()


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body_comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


LIKE_CHOICES = (('Like', 'Like'),
                ('Unlike', 'Unlike'))


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return self.post


class Images(models.Model):
    imagess = models.ImageField(upload_to="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
