from django.db import models

class Post(models.Model):
    image_url = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Anonymous")
    location = models.CharField(max_length=100, default="Unknown")
    caption_body = models.TextField(default="")
    likes = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100, default="Anonymous")
    comment_body = models.TextField(default="")
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author