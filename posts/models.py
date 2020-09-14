from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    view_count = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')
    #through : 두 개의 모델을 중간에서 관리하는 역할

    @property
    def like_count(self):
        return self.like_user_set.count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (('user', 'post'))

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    