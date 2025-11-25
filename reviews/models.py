from django.db import models
from django.contrib.auth.models import User
from components.models import Components
from cloudinary.models import CloudinaryField

# Create your models here.
class Review(models.Model):
    """
    Stores a single Review entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    component = models.ForeignKey(
        Components, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta: 
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Review by {self.author.username} | written by {self.component.name}"
    



class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`Review.Post`.
    """
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.content} by {self.author}"